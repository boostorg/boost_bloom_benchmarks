# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.36</td>
    <td align="right">4.78</td>
    <td align="right">3.83</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">10.53</td>
    <td align="right">10.03</td>
    <td align="right">15.98</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.80</td>
    <td align="right">4.11</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.61</td>
    <td align="right">4.80</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">15.85</td>
    <td align="right">14.50</td>
    <td align="right">16.93</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.49</td>
    <td align="right">4.62</td>
    <td align="right">4.63</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.11</td>
    <td align="right">5.18</td>
    <td align="right">5.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.20</td>
    <td align="right">17.71</td>
    <td align="right">16.01</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.18</td>
    <td align="right">5.11</td>
    <td align="right">5.09</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.01</td>
    <td align="right">6.03</td>
    <td align="right">6.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">25.52</td>
    <td align="right">22.97</td>
    <td align="right">16.50</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.99</td>
    <td align="right">5.73</td>
    <td align="right">5.76</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.58</td>
    <td align="right">6.40</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">4.84</td>
    <td align="right">5.11</td>
    <td align="right">5.12</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.10</td>
    <td align="right">5.79</td>
    <td align="right">5.71</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.80</td>
    <td align="right">3.09</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.16</td>
    <td align="right">7.75</td>
    <td align="right">7.74</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.71</td>
    <td align="right">8.85</td>
    <td align="right">8.86</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.33</td>
    <td align="right">2.96</td>
    <td align="right">2.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">8.99</td>
    <td align="right">12.42</td>
    <td align="right">12.40</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.82</td>
    <td align="right">13.14</td>
    <td align="right">13.12</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.53</td>
    <td align="right">5.72</td>
    <td align="right">3.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.85</td>
    <td align="right">14.44</td>
    <td align="right">14.57</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.01</td>
    <td align="right">16.44</td>
    <td align="right">16.43</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="right">3.82</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.78</td>
    <td align="right">3.03</td>
    <td align="right">3.05</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.20</td>
    <td align="right">4.86</td>
    <td align="right">4.79</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.35</td>
    <td align="right">4.75</td>
    <td align="right">4.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.90</td>
    <td align="right">3.13</td>
    <td align="right">3.14</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.95</td>
    <td align="right">4.20</td>
    <td align="right">4.22</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.24</td>
    <td align="right">4.78</td>
    <td align="right">4.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.26</td>
    <td align="right">5.29</td>
    <td align="right">3.67</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">6.78</td>
    <td align="right">7.39</td>
    <td align="right">5.65</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.54</td>
    <td align="right">7.30</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.32</td>
    <td align="right">5.34</td>
    <td align="right">3.68</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.78</td>
    <td align="right">8.83</td>
    <td align="right">5.84</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.17</td>
    <td align="right">8.72</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.41</td>
    <td align="right">15.43</td>
    <td align="right">22.14</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.47</td>
    <td align="right">10.09</td>
    <td align="right">20.56</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.00</td>
    <td align="right">13.43</td>
    <td align="right">21.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.75</td>
    <td align="right">15.51</td>
    <td align="right">23.11</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.83</td>
    <td align="right">14.69</td>
    <td align="right">20.92</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">11.82</td>
    <td align="right">13.48</td>
    <td align="right">21.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.38</td>
    <td align="right">18.96</td>
    <td align="right">24.19</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.60</td>
    <td align="right">15.53</td>
    <td align="right">20.61</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.96</td>
    <td align="right">17.08</td>
    <td align="right">21.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.09</td>
    <td align="right">22.89</td>
    <td align="right">24.98</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.00</td>
    <td align="right">14.47</td>
    <td align="right">20.23</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.39</td>
    <td align="right">18.24</td>
    <td align="right">21.43</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">33.17</td>
    <td align="right">18.93</td>
    <td align="right">7.20</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.14</td>
    <td align="right">13.15</td>
    <td align="right">17.82</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.81</td>
    <td align="right">5.23</td>
    <td align="right">6.08</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.04</td>
    <td align="right">6.10</td>
    <td align="right">6.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.11</td>
    <td align="right">20.02</td>
    <td align="right">18.38</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.50</td>
    <td align="right">6.94</td>
    <td align="right">7.52</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.20</td>
    <td align="right">6.54</td>
    <td align="right">6.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">32.62</td>
    <td align="right">31.49</td>
    <td align="right">19.05</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.48</td>
    <td align="right">11.41</td>
    <td align="right">7.57</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.76</td>
    <td align="right">12.88</td>
    <td align="right">8.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">56.91</td>
    <td align="right">54.37</td>
    <td align="right">22.81</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.53</td>
    <td align="right">15.28</td>
    <td align="right">18.06</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">18.14</td>
    <td align="right">15.59</td>
    <td align="right">13.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.54</td>
    <td align="right">7.26</td>
    <td align="right">7.20</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.29</td>
    <td align="right">8.08</td>
    <td align="right">7.76</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.59</td>
    <td align="right">4.19</td>
    <td align="right">4.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.58</td>
    <td align="right">12.03</td>
    <td align="right">11.50</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.36</td>
    <td align="right">12.23</td>
    <td align="right">13.74</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.96</td>
    <td align="right">3.89</td>
    <td align="right">3.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.73</td>
    <td align="right">19.25</td>
    <td align="right">17.01</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">25.42</td>
    <td align="right">21.67</td>
    <td align="right">19.66</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.32</td>
    <td align="right">7.83</td>
    <td align="right">5.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.81</td>
    <td align="right">22.52</td>
    <td align="right">19.62</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.73</td>
    <td align="right">22.28</td>
    <td align="right">23.16</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.00</td>
    <td align="right">10.03</td>
    <td align="right">7.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.55</td>
    <td align="right">3.98</td>
    <td align="right">4.00</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.17</td>
    <td align="right">6.05</td>
    <td align="right">5.98</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.33</td>
    <td align="right">5.95</td>
    <td align="right">6.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.51</td>
    <td align="right">3.93</td>
    <td align="right">4.02</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.68</td>
    <td align="right">5.32</td>
    <td align="right">5.20</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.97</td>
    <td align="right">5.91</td>
    <td align="right">5.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.57</td>
    <td align="right">7.23</td>
    <td align="right">5.48</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">9.56</td>
    <td align="right">10.14</td>
    <td align="right">7.88</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.63</td>
    <td align="right">9.99</td>
    <td align="right">7.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">12.64</td>
    <td align="right">10.35</td>
    <td align="right">6.83</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">12.44</td>
    <td align="right">13.97</td>
    <td align="right">10.41</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.46</td>
    <td align="right">21.01</td>
    <td align="right">10.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.11</td>
    <td align="right">17.14</td>
    <td align="right">26.51</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.36</td>
    <td align="right">12.40</td>
    <td align="right">23.13</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.66</td>
    <td align="right">15.42</td>
    <td align="right">24.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.30</td>
    <td align="right">19.53</td>
    <td align="right">26.34</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.48</td>
    <td align="right">15.85</td>
    <td align="right">23.08</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.44</td>
    <td align="right">15.54</td>
    <td align="right">23.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">14.03</td>
    <td align="right">22.63</td>
    <td align="right">34.26</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">23.57</td>
    <td align="right">21.40</td>
    <td align="right">24.68</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">30.09</td>
    <td align="right">38.72</td>
    <td align="right">34.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.59</td>
    <td align="right">32.40</td>
    <td align="right">37.14</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">22.15</td>
    <td align="right">24.98</td>
    <td align="right">26.20</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">34.17</td>
    <td align="right">34.21</td>
    <td align="right">37.00</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.53</td>
    <td align="right">4.16</td>
    <td align="right">3.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.68</td>
    <td align="right">8.60</td>
    <td align="right">14.75</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.18</td>
    <td align="right">3.74</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.77</td>
    <td align="right">4.45</td>
    <td align="right">4.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.44</td>
    <td align="right">12.48</td>
    <td align="right">15.81</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.65</td>
    <td align="right">4.33</td>
    <td align="right">4.49</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.31</td>
    <td align="right">5.29</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.64</td>
    <td align="right">15.21</td>
    <td align="right">14.96</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.13</td>
    <td align="right">4.84</td>
    <td align="right">4.86</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.35</td>
    <td align="right">5.84</td>
    <td align="right">5.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.53</td>
    <td align="right">18.97</td>
    <td align="right">15.37</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.82</td>
    <td align="right">5.48</td>
    <td align="right">5.48</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.71</td>
    <td align="right">3.07</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.88</td>
    <td align="right">3.39</td>
    <td align="right">3.38</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.99</td>
    <td align="right">3.27</td>
    <td align="right">3.28</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.45</td>
    <td align="right">2.36</td>
    <td align="right">2.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.57</td>
    <td align="right">3.86</td>
    <td align="right">3.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.47</td>
    <td align="right">4.13</td>
    <td align="right">4.13</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.03</td>
    <td align="right">2.14</td>
    <td align="right">2.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.26</td>
    <td align="right">6.72</td>
    <td align="right">6.71</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.45</td>
    <td align="right">6.56</td>
    <td align="right">6.54</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.95</td>
    <td align="right">4.08</td>
    <td align="right">2.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.70</td>
    <td align="right">7.40</td>
    <td align="right">7.31</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.95</td>
    <td align="right">7.71</td>
    <td align="right">7.65</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.94</td>
    <td align="right">4.12</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.44</td>
    <td align="right">2.19</td>
    <td align="right">2.22</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.37</td>
    <td align="right">3.83</td>
    <td align="right">3.82</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.53</td>
    <td align="right">3.70</td>
    <td align="right">3.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.55</td>
    <td align="right">2.26</td>
    <td align="right">2.26</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.67</td>
    <td align="right">3.51</td>
    <td align="right">3.50</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.57</td>
    <td align="right">3.77</td>
    <td align="right">3.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.95</td>
    <td align="right">3.98</td>
    <td align="right">2.75</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.18</td>
    <td align="right">5.82</td>
    <td align="right">4.85</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.38</td>
    <td align="right">5.63</td>
    <td align="right">4.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.00</td>
    <td align="right">4.01</td>
    <td align="right">2.75</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.47</td>
    <td align="right">6.82</td>
    <td align="right">5.29</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.58</td>
    <td align="right">6.78</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.31</td>
    <td align="right">14.85</td>
    <td align="right">22.36</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.35</td>
    <td align="right">9.74</td>
    <td align="right">19.94</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.24</td>
    <td align="right">11.72</td>
    <td align="right">21.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.74</td>
    <td align="right">15.57</td>
    <td align="right">23.56</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.84</td>
    <td align="right">11.96</td>
    <td align="right">20.38</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.40</td>
    <td align="right">12.23</td>
    <td align="right">21.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.40</td>
    <td align="right">17.13</td>
    <td align="right">24.63</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.03</td>
    <td align="right">13.55</td>
    <td align="right">21.44</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.31</td>
    <td align="right">16.34</td>
    <td align="right">22.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">13.90</td>
    <td align="right">17.70</td>
    <td align="right">24.63</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">13.88</td>
    <td align="right">15.84</td>
    <td align="right">20.04</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">16.96</td>
    <td align="right">17.90</td>
    <td align="right">22.24</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.73</td>
    <td align="right">15.88</td>
    <td align="right">6.41</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">10.96</td>
    <td align="right">10.58</td>
    <td align="right">16.38</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.12</td>
    <td align="right">4.67</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.54</td>
    <td align="right">5.32</td>
    <td align="right">5.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.12</td>
    <td align="right">15.43</td>
    <td align="right">17.03</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.26</td>
    <td align="right">4.94</td>
    <td align="right">5.09</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.64</td>
    <td align="right">5.68</td>
    <td align="right">5.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">21.48</td>
    <td align="right">22.80</td>
    <td align="right">16.66</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.26</td>
    <td align="right">6.07</td>
    <td align="right">6.25</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.84</td>
    <td align="right">7.41</td>
    <td align="right">7.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">37.43</td>
    <td align="right">38.97</td>
    <td align="right">18.30</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.43</td>
    <td align="right">9.19</td>
    <td align="right">10.92</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">6.27</td>
    <td align="right">5.73</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.60</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.71</td>
    <td align="right">4.10</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.04</td>
    <td align="right">2.99</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.10</td>
    <td align="right">4.58</td>
    <td align="right">4.79</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.05</td>
    <td align="right">4.89</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.44</td>
    <td align="right">2.66</td>
    <td align="right">2.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.96</td>
    <td align="right">8.94</td>
    <td align="right">9.28</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.31</td>
    <td align="right">9.16</td>
    <td align="right">14.54</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.28</td>
    <td align="right">5.75</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.46</td>
    <td align="right">11.55</td>
    <td align="right">11.88</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">9.28</td>
    <td align="right">12.50</td>
    <td align="right">12.14</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">11.14</td>
    <td align="right">12.82</td>
    <td align="right">8.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.12</td>
    <td align="right">2.94</td>
    <td align="right">2.97</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.25</td>
    <td align="right">4.80</td>
    <td align="right">4.84</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.46</td>
    <td align="right">4.76</td>
    <td align="right">4.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.18</td>
    <td align="right">3.12</td>
    <td align="right">3.17</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">4.19</td>
    <td align="right">4.29</td>
    <td align="right">4.30</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.11</td>
    <td align="right">4.16</td>
    <td align="right">4.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.34</td>
    <td align="right">6.14</td>
    <td align="right">4.11</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">7.37</td>
    <td align="right">7.83</td>
    <td align="right">6.69</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.12</td>
    <td align="right">7.58</td>
    <td align="right">6.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.40</td>
    <td align="right">8.35</td>
    <td align="right">5.38</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">10.63</td>
    <td align="right">12.11</td>
    <td align="right">8.42</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">9.46</td>
    <td align="right">14.04</td>
    <td align="right">7.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.97</td>
    <td align="right">17.12</td>
    <td align="right">25.86</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.99</td>
    <td align="right">11.68</td>
    <td align="right">22.47</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.95</td>
    <td align="right">14.45</td>
    <td align="right">23.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.49</td>
    <td align="right">17.85</td>
    <td align="right">27.05</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.49</td>
    <td align="right">15.26</td>
    <td align="right">27.71</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">15.78</td>
    <td align="right">14.54</td>
    <td align="right">25.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">15.11</td>
    <td align="right">23.41</td>
    <td align="right">34.21</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.28</td>
    <td align="right">19.19</td>
    <td align="right">32.56</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">23.62</td>
    <td align="right">23.86</td>
    <td align="right">34.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">25.37</td>
    <td align="right">28.57</td>
    <td align="right">37.53</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.05</td>
    <td align="right">25.67</td>
    <td align="right">36.44</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">39.35</td>
    <td align="right">34.37</td>
    <td align="right">42.08</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.64</td>
    <td align="right">7.39</td>
    <td align="right">4.34</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">10.03</td>
    <td align="right">10.13</td>
    <td align="right">14.26</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.85</td>
    <td align="right">1.79</td>
    <td align="right">1.41</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.94</td>
    <td align="right">1.99</td>
    <td align="right">1.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.07</td>
    <td align="right">8.09</td>
    <td align="right">16.08</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.67</td>
    <td align="right">1.64</td>
    <td align="right">1.62</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.38</td>
    <td align="right">1.84</td>
    <td align="right">1.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.91</td>
    <td align="right">13.47</td>
    <td align="right">13.71</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">2.62</td>
    <td align="right">2.19</td>
    <td align="right">3.43</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.14</td>
    <td align="right">2.63</td>
    <td align="right">2.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.11</td>
    <td align="right">12.82</td>
    <td align="right">12.44</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.24</td>
    <td align="right">2.57</td>
    <td align="right">3.65</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.22</td>
    <td align="right">1.94</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.75</td>
    <td align="right">2.03</td>
    <td align="right">2.13</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.80</td>
    <td align="right">2.12</td>
    <td align="right">2.06</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.16</td>
    <td align="right">2.91</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.30</td>
    <td align="right">2.64</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.34</td>
    <td align="right">3.43</td>
    <td align="right">2.56</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.04</td>
    <td align="right">2.36</td>
    <td align="right">1.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.68</td>
    <td align="right">3.29</td>
    <td align="right">5.50</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">7.13</td>
    <td align="right">3.89</td>
    <td align="right">5.61</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.69</td>
    <td align="right">2.77</td>
    <td align="right">2.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.51</td>
    <td align="right">4.11</td>
    <td align="right">4.12</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.58</td>
    <td align="right">4.94</td>
    <td align="right">4.83</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.47</td>
    <td align="right">5.83</td>
    <td align="right">3.21</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.29</td>
    <td align="right">1.95</td>
    <td align="right">1.96</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.71</td>
    <td align="right">2.11</td>
    <td align="right">1.96</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.66</td>
    <td align="right">2.04</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.43</td>
    <td align="right">2.01</td>
    <td align="right">2.26</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.57</td>
    <td align="right">2.33</td>
    <td align="right">2.81</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.33</td>
    <td align="right">2.66</td>
    <td align="right">2.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.35</td>
    <td align="right">2.79</td>
    <td align="right">1.96</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.97</td>
    <td align="right">3.39</td>
    <td align="right">3.68</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">7.33</td>
    <td align="right">3.51</td>
    <td align="right">4.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.50</td>
    <td align="right">3.66</td>
    <td align="right">2.03</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.74</td>
    <td align="right">4.52</td>
    <td align="right">4.57</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.63</td>
    <td align="right">4.94</td>
    <td align="right">4.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">4.00</td>
    <td align="right">20.81</td>
    <td align="right">24.37</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">4.30</td>
    <td align="right">18.74</td>
    <td align="right">26.45</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">9.77</td>
    <td align="right">15.89</td>
    <td align="right">22.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.07</td>
    <td align="right">22.98</td>
    <td align="right">30.34</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">6.97</td>
    <td align="right">15.14</td>
    <td align="right">23.95</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">9.70</td>
    <td align="right">14.55</td>
    <td align="right">24.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">9.16</td>
    <td align="right">20.29</td>
    <td align="right">27.58</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">12.70</td>
    <td align="right">18.45</td>
    <td align="right">21.26</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">10.53</td>
    <td align="right">21.41</td>
    <td align="right">23.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">9.56</td>
    <td align="right">25.44</td>
    <td align="right">27.15</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">9.76</td>
    <td align="right">20.82</td>
    <td align="right">25.67</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">14.22</td>
    <td align="right">25.71</td>
    <td align="right">25.49</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">33.12</td>
    <td align="right">15.98</td>
    <td align="right">10.37</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.41</td>
    <td align="right">13.75</td>
    <td align="right">26.81</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">8.40</td>
    <td align="right">8.43</td>
    <td align="right">6.63</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.74</td>
    <td align="right">4.81</td>
    <td align="right">4.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">37.21</td>
    <td align="right">39.19</td>
    <td align="right">27.48</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.03</td>
    <td align="right">8.06</td>
    <td align="right">10.42</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.07</td>
    <td align="right">9.04</td>
    <td align="right">8.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">76.18</td>
    <td align="right">53.00</td>
    <td align="right">31.87</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">14.63</td>
    <td align="right">13.98</td>
    <td align="right">12.09</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">13.14</td>
    <td align="right">16.23</td>
    <td align="right">15.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">111.06</td>
    <td align="right">88.81</td>
    <td align="right">46.36</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">20.67</td>
    <td align="right">17.48</td>
    <td align="right">16.33</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">16.43</td>
    <td align="right">13.61</td>
    <td align="right">12.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.35</td>
    <td align="right">4.84</td>
    <td align="right">6.57</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.82</td>
    <td align="right">8.99</td>
    <td align="right">8.56</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">6.97</td>
    <td align="right">8.68</td>
    <td align="right">7.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.36</td>
    <td align="right">14.79</td>
    <td align="right">12.80</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.78</td>
    <td align="right">14.32</td>
    <td align="right">14.59</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">9.11</td>
    <td align="right">11.48</td>
    <td align="right">10.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">27.93</td>
    <td align="right">21.93</td>
    <td align="right">20.47</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">26.10</td>
    <td align="right">21.97</td>
    <td align="right">21.66</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">18.62</td>
    <td align="right">18.29</td>
    <td align="right">12.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">31.67</td>
    <td align="right">27.06</td>
    <td align="right">25.00</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">31.15</td>
    <td align="right">29.08</td>
    <td align="right">29.35</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">18.62</td>
    <td align="right">22.83</td>
    <td align="right">13.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">6.16</td>
    <td align="right">6.36</td>
    <td align="right">6.93</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.99</td>
    <td align="right">7.67</td>
    <td align="right">6.87</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.20</td>
    <td align="right">9.58</td>
    <td align="right">8.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">9.83</td>
    <td align="right">9.37</td>
    <td align="right">10.31</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.93</td>
    <td align="right">13.02</td>
    <td align="right">14.18</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">13.38</td>
    <td align="right">14.18</td>
    <td align="right">14.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">19.66</td>
    <td align="right">18.89</td>
    <td align="right">12.00</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">24.36</td>
    <td align="right">16.86</td>
    <td align="right">15.97</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">22.01</td>
    <td align="right">15.92</td>
    <td align="right">15.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">14.87</td>
    <td align="right">17.73</td>
    <td align="right">10.16</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">25.44</td>
    <td align="right">21.32</td>
    <td align="right">27.61</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">30.67</td>
    <td align="right">28.94</td>
    <td align="right">27.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">16.93</td>
    <td align="right">32.22</td>
    <td align="right">39.18</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">16.89</td>
    <td align="right">22.16</td>
    <td align="right">38.41</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">25.89</td>
    <td align="right">25.21</td>
    <td align="right">38.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">26.48</td>
    <td align="right">41.04</td>
    <td align="right">47.53</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">21.26</td>
    <td align="right">24.80</td>
    <td align="right">30.99</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">28.34</td>
    <td align="right">29.52</td>
    <td align="right">35.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">27.48</td>
    <td align="right">40.54</td>
    <td align="right">47.35</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">25.35</td>
    <td align="right">34.68</td>
    <td align="right">39.56</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">40.04</td>
    <td align="right">42.57</td>
    <td align="right">44.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">34.14</td>
    <td align="right">40.62</td>
    <td align="right">47.29</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">30.37</td>
    <td align="right">35.71</td>
    <td align="right">39.41</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">44.07</td>
    <td align="right">50.29</td>
    <td align="right">46.71</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">36.35</td>
    <td align="right">5.61</td>
    <td align="right">3.55</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.04</td>
    <td align="right">12.49</td>
    <td align="right">16.95</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.79</td>
    <td align="right">4.19</td>
    <td align="right">4.19</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.94</td>
    <td align="right">5.19</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.18</td>
    <td align="right">17.49</td>
    <td align="right">17.64</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.87</td>
    <td align="right">4.70</td>
    <td align="right">4.72</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">7.95</td>
    <td align="right">5.88</td>
    <td align="right">6.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.36</td>
    <td align="right">21.10</td>
    <td align="right">16.56</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.58</td>
    <td align="right">5.28</td>
    <td align="right">5.26</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.26</td>
    <td align="right">6.55</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.75</td>
    <td align="right">26.71</td>
    <td align="right">17.48</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.88</td>
    <td align="right">5.87</td>
    <td align="right">5.86</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.30</td>
    <td align="right">7.36</td>
    <td align="right">7.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.85</td>
    <td align="right">5.50</td>
    <td align="right">5.48</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.14</td>
    <td align="right">5.51</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.35</td>
    <td align="right">3.91</td>
    <td align="right">3.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.23</td>
    <td align="right">8.19</td>
    <td align="right">8.21</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.36</td>
    <td align="right">7.78</td>
    <td align="right">8.62</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">3.19</td>
    <td align="right">4.83</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.43</td>
    <td align="right">10.99</td>
    <td align="right">10.70</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.80</td>
    <td align="right">10.85</td>
    <td align="right">10.37</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.92</td>
    <td align="right">7.04</td>
    <td align="right">5.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.33</td>
    <td align="right">14.21</td>
    <td align="right">14.27</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.84</td>
    <td align="right">12.49</td>
    <td align="right">13.45</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.01</td>
    <td align="right">7.11</td>
    <td align="right">5.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.30</td>
    <td align="right">3.80</td>
    <td align="right">3.79</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.45</td>
    <td align="right">5.42</td>
    <td align="right">5.41</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.62</td>
    <td align="right">5.34</td>
    <td align="right">5.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.22</td>
    <td align="right">5.53</td>
    <td align="right">4.61</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.72</td>
    <td align="right">5.84</td>
    <td align="right">5.00</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.92</td>
    <td align="right">6.94</td>
    <td align="right">6.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.99</td>
    <td align="right">6.74</td>
    <td align="right">4.99</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.72</td>
    <td align="right">9.04</td>
    <td align="right">7.38</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.75</td>
    <td align="right">9.20</td>
    <td align="right">7.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.07</td>
    <td align="right">6.87</td>
    <td align="right">5.08</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.11</td>
    <td align="right">10.60</td>
    <td align="right">7.60</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.03</td>
    <td align="right">10.43</td>
    <td align="right">7.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.95</td>
    <td align="right">21.49</td>
    <td align="right">27.32</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.77</td>
    <td align="right">14.37</td>
    <td align="right">24.08</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.61</td>
    <td align="right">16.26</td>
    <td align="right">24.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.60</td>
    <td align="right">25.62</td>
    <td align="right">28.15</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.89</td>
    <td align="right">16.75</td>
    <td align="right">25.89</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.79</td>
    <td align="right">18.17</td>
    <td align="right">24.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">13.93</td>
    <td align="right">27.22</td>
    <td align="right">29.27</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.61</td>
    <td align="right">18.68</td>
    <td align="right">25.44</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">18.17</td>
    <td align="right">21.90</td>
    <td align="right">24.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">18.35</td>
    <td align="right">26.89</td>
    <td align="right">30.35</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.60</td>
    <td align="right">21.89</td>
    <td align="right">25.04</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">21.25</td>
    <td align="right">24.45</td>
    <td align="right">25.22</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">39.83</td>
    <td align="right">20.11</td>
    <td align="right">7.38</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.34</td>
    <td align="right">12.99</td>
    <td align="right">17.59</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.96</td>
    <td align="right">4.50</td>
    <td align="right">4.45</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.81</td>
    <td align="right">5.52</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.01</td>
    <td align="right">18.69</td>
    <td align="right">18.40</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.48</td>
    <td align="right">5.06</td>
    <td align="right">5.04</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.13</td>
    <td align="right">6.28</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">27.52</td>
    <td align="right">23.18</td>
    <td align="right">17.26</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.17</td>
    <td align="right">5.79</td>
    <td align="right">5.71</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.76</td>
    <td align="right">7.38</td>
    <td align="right">9.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">74.39</td>
    <td align="right">57.14</td>
    <td align="right">20.74</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.80</td>
    <td align="right">9.43</td>
    <td align="right">9.23</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.88</td>
    <td align="right">9.12</td>
    <td align="right">9.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.28</td>
    <td align="right">6.20</td>
    <td align="right">6.18</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.37</td>
    <td align="right">6.25</td>
    <td align="right">6.22</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.74</td>
    <td align="right">4.15</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.36</td>
    <td align="right">9.70</td>
    <td align="right">9.72</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.29</td>
    <td align="right">8.52</td>
    <td align="right">9.27</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.11</td>
    <td align="right">5.84</td>
    <td align="right">4.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">17.61</td>
    <td align="right">12.43</td>
    <td align="right">12.48</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.12</td>
    <td align="right">11.64</td>
    <td align="right">11.42</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.84</td>
    <td align="right">7.83</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">22.52</td>
    <td align="right">20.89</td>
    <td align="right">19.75</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.33</td>
    <td align="right">14.49</td>
    <td align="right">15.39</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.30</td>
    <td align="right">9.47</td>
    <td align="right">7.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.72</td>
    <td align="right">4.05</td>
    <td align="right">4.04</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.93</td>
    <td align="right">5.81</td>
    <td align="right">5.80</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.04</td>
    <td align="right">5.69</td>
    <td align="right">5.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.67</td>
    <td align="right">5.93</td>
    <td align="right">5.00</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.34</td>
    <td align="right">6.28</td>
    <td align="right">5.35</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.72</td>
    <td align="right">7.42</td>
    <td align="right">6.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.10</td>
    <td align="right">7.79</td>
    <td align="right">5.92</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.93</td>
    <td align="right">10.44</td>
    <td align="right">8.66</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.67</td>
    <td align="right">10.08</td>
    <td align="right">8.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.45</td>
    <td align="right">9.36</td>
    <td align="right">6.86</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">13.35</td>
    <td align="right">13.43</td>
    <td align="right">10.15</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">15.60</td>
    <td align="right">16.74</td>
    <td align="right">12.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">10.08</td>
    <td align="right">23.15</td>
    <td align="right">29.50</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">9.71</td>
    <td align="right">15.00</td>
    <td align="right">25.50</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.18</td>
    <td align="right">17.29</td>
    <td align="right">25.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.52</td>
    <td align="right">26.81</td>
    <td align="right">30.34</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.70</td>
    <td align="right">17.16</td>
    <td align="right">27.17</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">14.61</td>
    <td align="right">20.02</td>
    <td align="right">26.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">15.25</td>
    <td align="right">28.58</td>
    <td align="right">31.21</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.50</td>
    <td align="right">20.00</td>
    <td align="right">27.82</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">20.52</td>
    <td align="right">23.89</td>
    <td align="right">26.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.82</td>
    <td align="right">30.50</td>
    <td align="right">34.95</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.47</td>
    <td align="right">24.75</td>
    <td align="right">28.46</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">26.63</td>
    <td align="right">30.98</td>
    <td align="right">30.80</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.00</td>
    <td align="right">31.96</td>
    <td align="right">16.82</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.23</td>
    <td align="right">41.97</td>
    <td align="right">36.49</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.50</td>
    <td align="right">15.56</td>
    <td align="right">15.55</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.16</td>
    <td align="right">20.13</td>
    <td align="right">19.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.75</td>
    <td align="right">63.42</td>
    <td align="right">39.34</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.31</td>
    <td align="right">19.58</td>
    <td align="right">19.59</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.18</td>
    <td align="right">18.67</td>
    <td align="right">18.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.62</td>
    <td align="right">78.76</td>
    <td align="right">38.39</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.41</td>
    <td align="right">18.51</td>
    <td align="right">18.46</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.18</td>
    <td align="right">18.29</td>
    <td align="right">18.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.43</td>
    <td align="right">96.45</td>
    <td align="right">37.67</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.13</td>
    <td align="right">18.81</td>
    <td align="right">18.83</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.95</td>
    <td align="right">19.88</td>
    <td align="right">19.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.13</td>
    <td align="right">21.26</td>
    <td align="right">21.25</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.69</td>
    <td align="right">22.23</td>
    <td align="right">22.20</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.94</td>
    <td align="right">13.57</td>
    <td align="right">13.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.26</td>
    <td align="right">25.99</td>
    <td align="right">26.01</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.37</td>
    <td align="right">27.43</td>
    <td align="right">27.43</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.82</td>
    <td align="right">15.64</td>
    <td align="right">15.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.10</td>
    <td align="right">32.86</td>
    <td align="right">32.88</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.64</td>
    <td align="right">46.48</td>
    <td align="right">46.54</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.91</td>
    <td align="right">19.53</td>
    <td align="right">19.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.12</td>
    <td align="right">35.78</td>
    <td align="right">35.78</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.62</td>
    <td align="right">56.26</td>
    <td align="right">56.35</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.08</td>
    <td align="right">25.57</td>
    <td align="right">25.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">15.44</td>
    <td align="right">15.56</td>
    <td align="right">15.53</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.17</td>
    <td align="right">21.22</td>
    <td align="right">21.24</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.52</td>
    <td align="right">22.13</td>
    <td align="right">22.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">20.02</td>
    <td align="right">20.46</td>
    <td align="right">20.47</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.28</td>
    <td align="right">25.94</td>
    <td align="right">25.97</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.50</td>
    <td align="right">27.58</td>
    <td align="right">27.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.25</td>
    <td align="right">24.84</td>
    <td align="right">24.86</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.12</td>
    <td align="right">32.97</td>
    <td align="right">32.96</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.68</td>
    <td align="right">46.62</td>
    <td align="right">46.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.19</td>
    <td align="right">37.07</td>
    <td align="right">37.05</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.18</td>
    <td align="right">35.85</td>
    <td align="right">35.75</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.55</td>
    <td align="right">56.18</td>
    <td align="right">56.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">12.95</td>
    <td align="right">32.36</td>
    <td align="right">37.64</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.12</td>
    <td align="right">27.17</td>
    <td align="right">35.30</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.07</td>
    <td align="right">42.70</td>
    <td align="right">48.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">20.55</td>
    <td align="right">38.25</td>
    <td align="right">43.27</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.05</td>
    <td align="right">43.26</td>
    <td align="right">45.90</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.36</td>
    <td align="right">59.94</td>
    <td align="right">56.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">23.71</td>
    <td align="right">42.74</td>
    <td align="right">44.32</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.60</td>
    <td align="right">47.97</td>
    <td align="right">47.19</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">46.83</td>
    <td align="right">74.54</td>
    <td align="right">62.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">27.51</td>
    <td align="right">45.60</td>
    <td align="right">46.97</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.35</td>
    <td align="right">52.42</td>
    <td align="right">52.01</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">48.91</td>
    <td align="right">68.77</td>
    <td align="right">61.51</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">72.05</td>
    <td align="right">105.40</td>
    <td align="right">20.47</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">27.56</td>
    <td align="right">42.66</td>
    <td align="right">39.06</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.78</td>
    <td align="right">15.53</td>
    <td align="right">15.54</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.33</td>
    <td align="right">19.24</td>
    <td align="right">19.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.39</td>
    <td align="right">62.29</td>
    <td align="right">40.36</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.28</td>
    <td align="right">19.88</td>
    <td align="right">19.88</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.98</td>
    <td align="right">18.82</td>
    <td align="right">18.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">43.66</td>
    <td align="right">75.99</td>
    <td align="right">38.54</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.46</td>
    <td align="right">23.96</td>
    <td align="right">18.71</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">18.23</td>
    <td align="right">18.58</td>
    <td align="right">18.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">56.50</td>
    <td align="right">97.92</td>
    <td align="right">39.80</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">18.63</td>
    <td align="right">19.29</td>
    <td align="right">19.68</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">19.53</td>
    <td align="right">20.43</td>
    <td align="right">20.98</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.41</td>
    <td align="right">21.66</td>
    <td align="right">21.69</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.86</td>
    <td align="right">22.82</td>
    <td align="right">22.84</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.03</td>
    <td align="right">13.82</td>
    <td align="right">13.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.06</td>
    <td align="right">25.37</td>
    <td align="right">25.39</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.47</td>
    <td align="right">27.96</td>
    <td align="right">27.98</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.65</td>
    <td align="right">15.55</td>
    <td align="right">15.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.35</td>
    <td align="right">33.68</td>
    <td align="right">33.82</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">65.70</td>
    <td align="right">48.46</td>
    <td align="right">50.11</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.68</td>
    <td align="right">19.73</td>
    <td align="right">19.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">40.01</td>
    <td align="right">46.60</td>
    <td align="right">37.55</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">80.98</td>
    <td align="right">58.32</td>
    <td align="right">58.46</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">27.87</td>
    <td align="right">26.99</td>
    <td align="right">26.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.79</td>
    <td align="right">15.87</td>
    <td align="right">15.88</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.44</td>
    <td align="right">21.66</td>
    <td align="right">21.76</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.14</td>
    <td align="right">23.04</td>
    <td align="right">23.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">19.65</td>
    <td align="right">20.15</td>
    <td align="right">20.19</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.18</td>
    <td align="right">25.38</td>
    <td align="right">25.42</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.53</td>
    <td align="right">28.30</td>
    <td align="right">28.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">28.50</td>
    <td align="right">24.63</td>
    <td align="right">24.70</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.94</td>
    <td align="right">44.26</td>
    <td align="right">45.48</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">71.56</td>
    <td align="right">53.64</td>
    <td align="right">52.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">68.24</td>
    <td align="right">76.35</td>
    <td align="right">55.39</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">59.69</td>
    <td align="right">37.92</td>
    <td align="right">38.47</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">107.91</td>
    <td align="right">76.49</td>
    <td align="right">76.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">12.99</td>
    <td align="right">32.33</td>
    <td align="right">40.02</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.57</td>
    <td align="right">27.92</td>
    <td align="right">37.59</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">32.94</td>
    <td align="right">45.42</td>
    <td align="right">52.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">20.78</td>
    <td align="right">42.02</td>
    <td align="right">45.13</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">27.19</td>
    <td align="right">43.29</td>
    <td align="right">46.76</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">39.14</td>
    <td align="right">61.41</td>
    <td align="right">58.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">23.82</td>
    <td align="right">44.25</td>
    <td align="right">45.71</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">33.11</td>
    <td align="right">48.75</td>
    <td align="right">49.28</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">51.53</td>
    <td align="right">87.05</td>
    <td align="right">81.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">29.92</td>
    <td align="right">56.46</td>
    <td align="right">59.80</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">67.14</td>
    <td align="right">82.69</td>
    <td align="right">117.21</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">128.09</td>
    <td align="right">137.63</td>
    <td align="right">120.05</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.14</td>
    <td align="right">10.50</td>
    <td align="right">7.86</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">14.06</td>
    <td align="right">23.03</td>
    <td align="right">26.82</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.65</td>
    <td align="right">12.50</td>
    <td align="right">12.48</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.87</td>
    <td align="right">14.14</td>
    <td align="right">14.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.98</td>
    <td align="right">35.47</td>
    <td align="right">28.98</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.22</td>
    <td align="right">14.34</td>
    <td align="right">14.30</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.66</td>
    <td align="right">15.62</td>
    <td align="right">15.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.45</td>
    <td align="right">47.80</td>
    <td align="right">30.49</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">14.00</td>
    <td align="right">15.81</td>
    <td align="right">15.69</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.82</td>
    <td align="right">16.90</td>
    <td align="right">17.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.82</td>
    <td align="right">60.95</td>
    <td align="right">31.27</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">15.08</td>
    <td align="right">16.54</td>
    <td align="right">16.53</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">16.19</td>
    <td align="right">18.04</td>
    <td align="right">18.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.79</td>
    <td align="right">16.17</td>
    <td align="right">16.22</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.24</td>
    <td align="right">16.77</td>
    <td align="right">16.77</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.16</td>
    <td align="right">9.40</td>
    <td align="right">9.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.28</td>
    <td align="right">21.81</td>
    <td align="right">21.71</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.36</td>
    <td align="right">22.26</td>
    <td align="right">22.29</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">10.87</td>
    <td align="right">14.03</td>
    <td align="right">14.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.14</td>
    <td align="right">32.34</td>
    <td align="right">32.30</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.90</td>
    <td align="right">30.77</td>
    <td align="right">30.79</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.31</td>
    <td align="right">17.53</td>
    <td align="right">17.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.11</td>
    <td align="right">35.95</td>
    <td align="right">36.05</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.17</td>
    <td align="right">35.95</td>
    <td align="right">36.01</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.41</td>
    <td align="right">20.57</td>
    <td align="right">20.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.60</td>
    <td align="right">9.46</td>
    <td align="right">9.45</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.70</td>
    <td align="right">16.19</td>
    <td align="right">16.15</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.29</td>
    <td align="right">16.94</td>
    <td align="right">16.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">12.32</td>
    <td align="right">13.70</td>
    <td align="right">13.90</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.49</td>
    <td align="right">22.45</td>
    <td align="right">22.41</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.42</td>
    <td align="right">22.29</td>
    <td align="right">22.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.31</td>
    <td align="right">17.63</td>
    <td align="right">17.66</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.05</td>
    <td align="right">32.30</td>
    <td align="right">32.31</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.84</td>
    <td align="right">30.85</td>
    <td align="right">30.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.20</td>
    <td align="right">20.88</td>
    <td align="right">21.52</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.08</td>
    <td align="right">35.97</td>
    <td align="right">36.01</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.29</td>
    <td align="right">36.01</td>
    <td align="right">36.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">11.67</td>
    <td align="right">27.17</td>
    <td align="right">35.47</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.28</td>
    <td align="right">29.83</td>
    <td align="right">34.20</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.64</td>
    <td align="right">33.70</td>
    <td align="right">38.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">14.97</td>
    <td align="right">28.63</td>
    <td align="right">36.82</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.84</td>
    <td align="right">39.20</td>
    <td align="right">40.90</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">53.42</td>
    <td align="right">52.20</td>
    <td align="right">48.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">18.14</td>
    <td align="right">28.59</td>
    <td align="right">37.82</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.31</td>
    <td align="right">43.51</td>
    <td align="right">43.46</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.78</td>
    <td align="right">62.66</td>
    <td align="right">60.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">20.45</td>
    <td align="right">33.35</td>
    <td align="right">39.24</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">30.40</td>
    <td align="right">44.90</td>
    <td align="right">45.77</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">65.94</td>
    <td align="right">51.25</td>
    <td align="right">53.53</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">91.61</td>
    <td align="right">51.74</td>
    <td align="right">11.31</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.23</td>
    <td align="right">22.92</td>
    <td align="right">28.35</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.71</td>
    <td align="right">12.68</td>
    <td align="right">12.66</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.97</td>
    <td align="right">14.03</td>
    <td align="right">14.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.51</td>
    <td align="right">34.85</td>
    <td align="right">29.56</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.27</td>
    <td align="right">14.02</td>
    <td align="right">14.21</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.47</td>
    <td align="right">15.36</td>
    <td align="right">15.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.73</td>
    <td align="right">48.33</td>
    <td align="right">30.54</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">14.48</td>
    <td align="right">16.71</td>
    <td align="right">15.06</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">39.56</td>
    <td align="right">19.61</td>
    <td align="right">17.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">41.25</td>
    <td align="right">88.29</td>
    <td align="right">31.76</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">15.58</td>
    <td align="right">17.38</td>
    <td align="right">16.87</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">16.86</td>
    <td align="right">19.56</td>
    <td align="right">18.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.14</td>
    <td align="right">16.69</td>
    <td align="right">16.69</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">14.38</td>
    <td align="right">17.77</td>
    <td align="right">17.54</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.30</td>
    <td align="right">9.45</td>
    <td align="right">9.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.30</td>
    <td align="right">22.38</td>
    <td align="right">22.54</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">19.11</td>
    <td align="right">22.90</td>
    <td align="right">23.44</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.39</td>
    <td align="right">14.14</td>
    <td align="right">14.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">25.72</td>
    <td align="right">44.21</td>
    <td align="right">75.67</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">28.17</td>
    <td align="right">33.87</td>
    <td align="right">32.69</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.78</td>
    <td align="right">19.69</td>
    <td align="right">19.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">43.66</td>
    <td align="right">52.67</td>
    <td align="right">54.96</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">54.30</td>
    <td align="right">42.38</td>
    <td align="right">48.57</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">30.00</td>
    <td align="right">30.54</td>
    <td align="right">21.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.74</td>
    <td align="right">9.57</td>
    <td align="right">9.56</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.19</td>
    <td align="right">16.65</td>
    <td align="right">16.62</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.51</td>
    <td align="right">18.64</td>
    <td align="right">17.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">12.05</td>
    <td align="right">13.53</td>
    <td align="right">13.48</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.03</td>
    <td align="right">22.03</td>
    <td align="right">22.03</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.49</td>
    <td align="right">22.02</td>
    <td align="right">22.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">27.04</td>
    <td align="right">38.68</td>
    <td align="right">22.23</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">26.49</td>
    <td align="right">35.94</td>
    <td align="right">33.35</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">27.31</td>
    <td align="right">32.57</td>
    <td align="right">33.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">20.87</td>
    <td align="right">44.10</td>
    <td align="right">22.71</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">27.61</td>
    <td align="right">38.07</td>
    <td align="right">38.18</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">36.23</td>
    <td align="right">65.81</td>
    <td align="right">43.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">12.32</td>
    <td align="right">26.59</td>
    <td align="right">37.76</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">13.53</td>
    <td align="right">29.78</td>
    <td align="right">37.19</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">49.54</td>
    <td align="right">35.52</td>
    <td align="right">40.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">18.27</td>
    <td align="right">37.02</td>
    <td align="right">41.46</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">20.69</td>
    <td align="right">41.07</td>
    <td align="right">43.73</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">55.36</td>
    <td align="right">54.25</td>
    <td align="right">49.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">18.47</td>
    <td align="right">28.88</td>
    <td align="right">39.04</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">24.29</td>
    <td align="right">44.48</td>
    <td align="right">53.41</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">76.75</td>
    <td align="right">91.12</td>
    <td align="right">80.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">23.68</td>
    <td align="right">38.31</td>
    <td align="right">79.74</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">33.63</td>
    <td align="right">61.64</td>
    <td align="right">59.43</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">76.07</td>
    <td align="right">59.89</td>
    <td align="right">61.71</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">41.95</td>
    <td align="right">8.53</td>
    <td align="right">6.65</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.41</td>
    <td align="right">54.72</td>
    <td align="right">41.41</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.87</td>
    <td align="right">23.05</td>
    <td align="right">26.60</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.59</td>
    <td align="right">25.88</td>
    <td align="right">29.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.75</td>
    <td align="right">80.90</td>
    <td align="right">44.04</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.90</td>
    <td align="right">23.90</td>
    <td align="right">26.21</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.05</td>
    <td align="right">27.62</td>
    <td align="right">30.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.52</td>
    <td align="right">98.01</td>
    <td align="right">43.31</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.38</td>
    <td align="right">24.90</td>
    <td align="right">26.62</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.63</td>
    <td align="right">30.55</td>
    <td align="right">31.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">140.53</td>
    <td align="right">123.61</td>
    <td align="right">44.04</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.56</td>
    <td align="right">27.39</td>
    <td align="right">28.07</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.23</td>
    <td align="right">32.82</td>
    <td align="right">34.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.55</td>
    <td align="right">43.14</td>
    <td align="right">43.08</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.53</td>
    <td align="right">43.47</td>
    <td align="right">43.86</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.58</td>
    <td align="right">24.93</td>
    <td align="right">24.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.55</td>
    <td align="right">58.61</td>
    <td align="right">58.89</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.96</td>
    <td align="right">60.10</td>
    <td align="right">59.81</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.56</td>
    <td align="right">36.53</td>
    <td align="right">25.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.01</td>
    <td align="right">80.10</td>
    <td align="right">80.69</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.98</td>
    <td align="right">84.66</td>
    <td align="right">80.59</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.04</td>
    <td align="right">55.08</td>
    <td align="right">39.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">43.85</td>
    <td align="right">88.91</td>
    <td align="right">88.75</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.23</td>
    <td align="right">95.17</td>
    <td align="right">96.29</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.15</td>
    <td align="right">55.66</td>
    <td align="right">40.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.64</td>
    <td align="right">26.15</td>
    <td align="right">26.28</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.67</td>
    <td align="right">29.03</td>
    <td align="right">29.17</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.89</td>
    <td align="right">31.09</td>
    <td align="right">31.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.99</td>
    <td align="right">46.85</td>
    <td align="right">35.01</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.42</td>
    <td align="right">40.50</td>
    <td align="right">27.45</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">20.98</td>
    <td align="right">51.87</td>
    <td align="right">40.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.78</td>
    <td align="right">54.70</td>
    <td align="right">39.27</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.01</td>
    <td align="right">52.99</td>
    <td align="right">35.13</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.07</td>
    <td align="right">61.31</td>
    <td align="right">43.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.72</td>
    <td align="right">55.54</td>
    <td align="right">39.38</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.54</td>
    <td align="right">64.36</td>
    <td align="right">44.20</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.34</td>
    <td align="right">64.31</td>
    <td align="right">44.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">23.49</td>
    <td align="right">32.01</td>
    <td align="right">42.74</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.25</td>
    <td align="right">35.66</td>
    <td align="right">44.81</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">32.27</td>
    <td align="right">45.84</td>
    <td align="right">52.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">33.43</td>
    <td align="right">46.45</td>
    <td align="right">48.20</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">35.83</td>
    <td align="right">44.47</td>
    <td align="right">54.17</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">42.20</td>
    <td align="right">54.79</td>
    <td align="right">61.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">38.07</td>
    <td align="right">48.59</td>
    <td align="right">51.50</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">40.89</td>
    <td align="right">50.54</td>
    <td align="right">56.99</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.30</td>
    <td align="right">59.24</td>
    <td align="right">67.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">46.38</td>
    <td align="right">52.09</td>
    <td align="right">62.63</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">51.95</td>
    <td align="right">59.24</td>
    <td align="right">66.58</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">58.31</td>
    <td align="right">69.56</td>
    <td align="right">77.60</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.03</td>
    <td align="right">38.12</td>
    <td align="right">10.92</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">67.00</td>
    <td align="right">59.77</td>
    <td align="right">46.29</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.16</td>
    <td align="right">23.29</td>
    <td align="right">28.35</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">27.78</td>
    <td align="right">29.43</td>
    <td align="right">33.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">97.51</td>
    <td align="right">86.19</td>
    <td align="right">47.87</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.73</td>
    <td align="right">24.37</td>
    <td align="right">27.34</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">29.81</td>
    <td align="right">31.08</td>
    <td align="right">33.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">131.91</td>
    <td align="right">113.89</td>
    <td align="right">48.01</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">28.26</td>
    <td align="right">26.25</td>
    <td align="right">28.17</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">35.39</td>
    <td align="right">35.39</td>
    <td align="right">38.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">193.69</td>
    <td align="right">172.85</td>
    <td align="right">53.72</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">34.18</td>
    <td align="right">31.67</td>
    <td align="right">31.84</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">41.72</td>
    <td align="right">40.96</td>
    <td align="right">44.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.62</td>
    <td align="right">43.74</td>
    <td align="right">43.85</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">29.95</td>
    <td align="right">44.61</td>
    <td align="right">44.77</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">19.92</td>
    <td align="right">29.50</td>
    <td align="right">29.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.43</td>
    <td align="right">59.75</td>
    <td align="right">59.94</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.01</td>
    <td align="right">60.92</td>
    <td align="right">60.78</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.06</td>
    <td align="right">40.83</td>
    <td align="right">29.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">43.66</td>
    <td align="right">81.58</td>
    <td align="right">82.07</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">49.93</td>
    <td align="right">87.38</td>
    <td align="right">83.61</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">33.02</td>
    <td align="right">62.78</td>
    <td align="right">45.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">52.26</td>
    <td align="right">97.69</td>
    <td align="right">96.04</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">60.53</td>
    <td align="right">103.16</td>
    <td align="right">103.53</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">42.06</td>
    <td align="right">71.85</td>
    <td align="right">54.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">19.82</td>
    <td align="right">31.31</td>
    <td align="right">31.14</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">21.73</td>
    <td align="right">33.57</td>
    <td align="right">33.62</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">21.83</td>
    <td align="right">35.79</td>
    <td align="right">35.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.39</td>
    <td align="right">51.99</td>
    <td align="right">40.44</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.21</td>
    <td align="right">42.55</td>
    <td align="right">30.86</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">23.85</td>
    <td align="right">59.09</td>
    <td align="right">47.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">32.26</td>
    <td align="right">64.16</td>
    <td align="right">45.55</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">35.21</td>
    <td align="right">58.01</td>
    <td align="right">39.66</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">34.22</td>
    <td align="right">67.08</td>
    <td align="right">49.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">39.18</td>
    <td align="right">69.17</td>
    <td align="right">51.56</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">40.53</td>
    <td align="right">74.59</td>
    <td align="right">53.21</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">38.71</td>
    <td align="right">75.32</td>
    <td align="right">54.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">25.85</td>
    <td align="right">33.73</td>
    <td align="right">47.11</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">27.73</td>
    <td align="right">36.63</td>
    <td align="right">47.04</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">36.71</td>
    <td align="right">50.64</td>
    <td align="right">56.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">36.27</td>
    <td align="right">47.51</td>
    <td align="right">50.50</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">39.91</td>
    <td align="right">46.03</td>
    <td align="right">54.91</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">47.88</td>
    <td align="right">59.58</td>
    <td align="right">65.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">42.69</td>
    <td align="right">50.96</td>
    <td align="right">54.01</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">46.30</td>
    <td align="right">52.59</td>
    <td align="right">59.76</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">55.07</td>
    <td align="right">64.82</td>
    <td align="right">76.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">55.71</td>
    <td align="right">57.85</td>
    <td align="right">68.72</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">60.49</td>
    <td align="right">64.13</td>
    <td align="right">71.69</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">75.51</td>
    <td align="right">87.81</td>
    <td align="right">95.71</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
