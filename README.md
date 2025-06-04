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
    <td align="right">26.81</td>
    <td align="right">4.65</td>
    <td align="right">3.82</td>
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
    <td align="right">11.34</td>
    <td align="right">10.65</td>
    <td align="right">16.64</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.05</td>
    <td align="right">4.39</td>
    <td align="right">4.38</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.87</td>
    <td align="right">5.19</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.77</td>
    <td align="right">15.60</td>
    <td align="right">17.68</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.83</td>
    <td align="right">4.97</td>
    <td align="right">5.01</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.45</td>
    <td align="right">5.54</td>
    <td align="right">5.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.80</td>
    <td align="right">18.75</td>
    <td align="right">16.52</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.44</td>
    <td align="right">5.36</td>
    <td align="right">5.35</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.28</td>
    <td align="right">6.32</td>
    <td align="right">6.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.44</td>
    <td align="right">23.00</td>
    <td align="right">16.86</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.26</td>
    <td align="right">5.99</td>
    <td align="right">6.00</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.72</td>
    <td align="right">6.61</td>
    <td align="right">6.60</td>
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
    <td align="right">5.11</td>
    <td align="right">5.76</td>
    <td align="right">5.75</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.31</td>
    <td align="right">6.60</td>
    <td align="right">6.52</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.97</td>
    <td align="right">3.28</td>
    <td align="right">3.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.56</td>
    <td align="right">8.89</td>
    <td align="right">8.89</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.29</td>
    <td align="right">9.93</td>
    <td align="right">10.10</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.49</td>
    <td align="right">3.13</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.31</td>
    <td align="right">13.78</td>
    <td align="right">13.80</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.75</td>
    <td align="right">14.16</td>
    <td align="right">14.13</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.77</td>
    <td align="right">5.80</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.15</td>
    <td align="right">15.41</td>
    <td align="right">15.41</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.29</td>
    <td align="right">17.40</td>
    <td align="right">17.36</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.83</td>
    <td align="right">5.83</td>
    <td align="right">3.90</td>
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
    <td align="right">2.93</td>
    <td align="right">3.23</td>
    <td align="right">3.24</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.42</td>
    <td align="right">5.12</td>
    <td align="right">5.04</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.62</td>
    <td align="right">4.99</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.03</td>
    <td align="right">3.31</td>
    <td align="right">3.33</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.21</td>
    <td align="right">4.48</td>
    <td align="right">4.49</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.51</td>
    <td align="right">5.12</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.48</td>
    <td align="right">5.51</td>
    <td align="right">3.77</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.08</td>
    <td align="right">7.74</td>
    <td align="right">5.93</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.95</td>
    <td align="right">7.56</td>
    <td align="right">5.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.53</td>
    <td align="right">5.55</td>
    <td align="right">3.81</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.12</td>
    <td align="right">9.19</td>
    <td align="right">6.01</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.35</td>
    <td align="right">9.07</td>
    <td align="right">5.91</td>
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
    <td align="right">6.85</td>
    <td align="right">21.81</td>
    <td align="right">21.47</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.92</td>
    <td align="right">14.69</td>
    <td align="right">14.70</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.50</td>
    <td align="right">18.92</td>
    <td align="right">19.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.34</td>
    <td align="right">25.15</td>
    <td align="right">25.24</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.42</td>
    <td align="right">17.15</td>
    <td align="right">17.89</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.33</td>
    <td align="right">20.36</td>
    <td align="right">20.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.85</td>
    <td align="right">27.66</td>
    <td align="right">27.73</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.04</td>
    <td align="right">18.71</td>
    <td align="right">18.73</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.50</td>
    <td align="right">21.88</td>
    <td align="right">21.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.42</td>
    <td align="right">25.03</td>
    <td align="right">25.24</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.55</td>
    <td align="right">18.86</td>
    <td align="right">18.84</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">18.07</td>
    <td align="right">23.42</td>
    <td align="right">23.45</td>
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
    <td align="right">33.67</td>
    <td align="right">20.77</td>
    <td align="right">6.94</td>
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
    <td align="right">14.11</td>
    <td align="right">13.11</td>
    <td align="right">17.90</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.84</td>
    <td align="right">5.15</td>
    <td align="right">5.15</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.90</td>
    <td align="right">6.08</td>
    <td align="right">6.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.69</td>
    <td align="right">18.91</td>
    <td align="right">18.44</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.73</td>
    <td align="right">5.78</td>
    <td align="right">6.04</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.44</td>
    <td align="right">6.47</td>
    <td align="right">6.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">27.32</td>
    <td align="right">27.64</td>
    <td align="right">17.84</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.64</td>
    <td align="right">7.26</td>
    <td align="right">6.47</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.58</td>
    <td align="right">9.18</td>
    <td align="right">7.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">53.35</td>
    <td align="right">50.40</td>
    <td align="right">21.74</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">18.62</td>
    <td align="right">16.71</td>
    <td align="right">16.46</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">18.95</td>
    <td align="right">16.17</td>
    <td align="right">13.53</td>
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
    <td align="right">5.86</td>
    <td align="right">6.70</td>
    <td align="right">6.63</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.30</td>
    <td align="right">7.96</td>
    <td align="right">7.94</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.52</td>
    <td align="right">3.98</td>
    <td align="right">4.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.61</td>
    <td align="right">10.03</td>
    <td align="right">9.90</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.70</td>
    <td align="right">11.66</td>
    <td align="right">11.14</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.23</td>
    <td align="right">3.91</td>
    <td align="right">3.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">13.00</td>
    <td align="right">17.85</td>
    <td align="right">16.79</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.43</td>
    <td align="right">16.02</td>
    <td align="right">17.90</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.72</td>
    <td align="right">8.76</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.23</td>
    <td align="right">19.46</td>
    <td align="right">20.52</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.14</td>
    <td align="right">25.23</td>
    <td align="right">21.94</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.25</td>
    <td align="right">15.66</td>
    <td align="right">12.98</td>
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
    <td align="right">3.63</td>
    <td align="right">4.06</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.25</td>
    <td align="right">6.23</td>
    <td align="right">6.10</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.40</td>
    <td align="right">6.08</td>
    <td align="right">6.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.71</td>
    <td align="right">4.06</td>
    <td align="right">3.91</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.79</td>
    <td align="right">5.46</td>
    <td align="right">5.21</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">5.22</td>
    <td align="right">5.93</td>
    <td align="right">5.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.97</td>
    <td align="right">7.27</td>
    <td align="right">5.13</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">9.69</td>
    <td align="right">10.31</td>
    <td align="right">7.90</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.41</td>
    <td align="right">11.06</td>
    <td align="right">7.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">11.63</td>
    <td align="right">15.92</td>
    <td align="right">11.25</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">18.10</td>
    <td align="right">13.17</td>
    <td align="right">9.17</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.45</td>
    <td align="right">14.26</td>
    <td align="right">10.01</td>
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
    <td align="right">8.34</td>
    <td align="right">24.55</td>
    <td align="right">24.93</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.42</td>
    <td align="right">17.12</td>
    <td align="right">17.49</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.93</td>
    <td align="right">23.34</td>
    <td align="right">23.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.46</td>
    <td align="right">36.81</td>
    <td align="right">33.94</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.84</td>
    <td align="right">18.66</td>
    <td align="right">20.77</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.83</td>
    <td align="right">25.68</td>
    <td align="right">23.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">14.56</td>
    <td align="right">34.71</td>
    <td align="right">33.64</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">13.21</td>
    <td align="right">19.87</td>
    <td align="right">22.64</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">22.30</td>
    <td align="right">29.12</td>
    <td align="right">33.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">30.67</td>
    <td align="right">48.75</td>
    <td align="right">41.95</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">26.82</td>
    <td align="right">27.48</td>
    <td align="right">28.07</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">34.78</td>
    <td align="right">47.89</td>
    <td align="right">35.57</td>
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
    <td align="right">25.99</td>
    <td align="right">4.05</td>
    <td align="right">3.28</td>
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
    <td align="right">9.15</td>
    <td align="right">8.89</td>
    <td align="right">16.48</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.31</td>
    <td align="right">3.94</td>
    <td align="right">4.05</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.86</td>
    <td align="right">4.67</td>
    <td align="right">4.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.06</td>
    <td align="right">13.52</td>
    <td align="right">16.56</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.85</td>
    <td align="right">4.57</td>
    <td align="right">4.73</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.48</td>
    <td align="right">5.50</td>
    <td align="right">5.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.27</td>
    <td align="right">16.74</td>
    <td align="right">15.58</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.33</td>
    <td align="right">5.07</td>
    <td align="right">5.08</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.93</td>
    <td align="right">5.98</td>
    <td align="right">5.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.89</td>
    <td align="right">20.54</td>
    <td align="right">16.00</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.80</td>
    <td align="right">5.66</td>
    <td align="right">5.67</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.82</td>
    <td align="right">3.27</td>
    <td align="right">3.26</td>
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
    <td align="right">3.05</td>
    <td align="right">3.59</td>
    <td align="right">3.59</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.16</td>
    <td align="right">3.49</td>
    <td align="right">3.48</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.57</td>
    <td align="right">2.46</td>
    <td align="right">2.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.07</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.70</td>
    <td align="right">4.35</td>
    <td align="right">4.34</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.12</td>
    <td align="right">2.24</td>
    <td align="right">2.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.57</td>
    <td align="right">7.14</td>
    <td align="right">7.14</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.78</td>
    <td align="right">6.98</td>
    <td align="right">6.96</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.16</td>
    <td align="right">4.35</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.00</td>
    <td align="right">7.75</td>
    <td align="right">7.73</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.32</td>
    <td align="right">8.16</td>
    <td align="right">8.06</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.22</td>
    <td align="right">4.37</td>
    <td align="right">3.11</td>
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
    <td align="right">2.59</td>
    <td align="right">2.32</td>
    <td align="right">2.34</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.58</td>
    <td align="right">4.05</td>
    <td align="right">4.04</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.74</td>
    <td align="right">3.91</td>
    <td align="right">3.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.69</td>
    <td align="right">2.38</td>
    <td align="right">2.39</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.86</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.82</td>
    <td align="right">4.02</td>
    <td align="right">4.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.25</td>
    <td align="right">4.27</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.58</td>
    <td align="right">6.11</td>
    <td align="right">4.62</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.71</td>
    <td align="right">5.94</td>
    <td align="right">4.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.27</td>
    <td align="right">4.29</td>
    <td align="right">2.91</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.79</td>
    <td align="right">7.12</td>
    <td align="right">4.63</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.97</td>
    <td align="right">7.18</td>
    <td align="right">4.56</td>
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
    <td align="right">6.71</td>
    <td align="right">15.11</td>
    <td align="right">15.12</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.82</td>
    <td align="right">16.16</td>
    <td align="right">15.87</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.22</td>
    <td align="right">16.07</td>
    <td align="right">16.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.26</td>
    <td align="right">15.51</td>
    <td align="right">15.49</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.40</td>
    <td align="right">15.72</td>
    <td align="right">15.68</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.14</td>
    <td align="right">15.17</td>
    <td align="right">15.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.85</td>
    <td align="right">15.50</td>
    <td align="right">15.78</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.59</td>
    <td align="right">16.16</td>
    <td align="right">16.17</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.95</td>
    <td align="right">16.54</td>
    <td align="right">16.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.66</td>
    <td align="right">17.51</td>
    <td align="right">17.61</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.76</td>
    <td align="right">17.39</td>
    <td align="right">17.34</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.75</td>
    <td align="right">16.92</td>
    <td align="right">16.92</td>
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
    <td align="right">31.66</td>
    <td align="right">14.94</td>
    <td align="right">5.82</td>
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
    <td align="right">11.10</td>
    <td align="right">10.74</td>
    <td align="right">16.52</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.93</td>
    <td align="right">4.59</td>
    <td align="right">4.69</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.60</td>
    <td align="right">5.43</td>
    <td align="right">5.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.24</td>
    <td align="right">15.57</td>
    <td align="right">17.32</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.40</td>
    <td align="right">5.11</td>
    <td align="right">5.24</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.14</td>
    <td align="right">6.05</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">19.62</td>
    <td align="right">19.64</td>
    <td align="right">16.39</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.20</td>
    <td align="right">5.84</td>
    <td align="right">5.98</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.80</td>
    <td align="right">6.88</td>
    <td align="right">6.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">28.53</td>
    <td align="right">28.96</td>
    <td align="right">17.16</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">6.38</td>
    <td align="right">7.11</td>
    <td align="right">6.79</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.12</td>
    <td align="right">4.79</td>
    <td align="right">4.65</td>
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
    <td align="right">3.70</td>
    <td align="right">4.35</td>
    <td align="right">4.35</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.78</td>
    <td align="right">4.23</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.11</td>
    <td align="right">3.12</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.14</td>
    <td align="right">4.85</td>
    <td align="right">4.66</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.15</td>
    <td align="right">5.03</td>
    <td align="right">5.04</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.54</td>
    <td align="right">2.67</td>
    <td align="right">2.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.89</td>
    <td align="right">8.73</td>
    <td align="right">8.76</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.00</td>
    <td align="right">8.69</td>
    <td align="right">8.75</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">4.93</td>
    <td align="right">5.35</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.03</td>
    <td align="right">10.16</td>
    <td align="right">10.19</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">8.44</td>
    <td align="right">11.08</td>
    <td align="right">10.81</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.11</td>
    <td align="right">7.81</td>
    <td align="right">5.72</td>
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
    <td align="right">3.15</td>
    <td align="right">2.99</td>
    <td align="right">3.00</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.36</td>
    <td align="right">4.95</td>
    <td align="right">4.95</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.36</td>
    <td align="right">4.65</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.08</td>
    <td align="right">2.99</td>
    <td align="right">2.92</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.33</td>
    <td align="right">4.24</td>
    <td align="right">4.23</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.31</td>
    <td align="right">4.72</td>
    <td align="right">4.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.05</td>
    <td align="right">5.35</td>
    <td align="right">3.79</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.78</td>
    <td align="right">7.67</td>
    <td align="right">6.38</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">6.97</td>
    <td align="right">7.59</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">6.28</td>
    <td align="right">6.78</td>
    <td align="right">4.64</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">8.99</td>
    <td align="right">9.91</td>
    <td align="right">7.10</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">9.04</td>
    <td align="right">9.65</td>
    <td align="right">6.72</td>
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
    <td align="right">8.06</td>
    <td align="right">13.87</td>
    <td align="right">13.86</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.13</td>
    <td align="right">14.25</td>
    <td align="right">14.31</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.79</td>
    <td align="right">14.41</td>
    <td align="right">14.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.39</td>
    <td align="right">14.77</td>
    <td align="right">14.80</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.65</td>
    <td align="right">15.43</td>
    <td align="right">15.41</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.65</td>
    <td align="right">15.82</td>
    <td align="right">15.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">12.74</td>
    <td align="right">16.67</td>
    <td align="right">16.85</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">13.19</td>
    <td align="right">17.18</td>
    <td align="right">17.26</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">29.19</td>
    <td align="right">17.68</td>
    <td align="right">17.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">17.67</td>
    <td align="right">18.89</td>
    <td align="right">18.98</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">17.61</td>
    <td align="right">18.72</td>
    <td align="right">18.86</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">32.40</td>
    <td align="right">24.73</td>
    <td align="right">20.99</td>
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
    <td align="right">22.47</td>
    <td align="right">4.61</td>
    <td align="right">3.45</td>
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
    <td align="right">7.37</td>
    <td align="right">5.23</td>
    <td align="right">11.74</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.44</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.65</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.38</td>
    <td align="right">7.55</td>
    <td align="right">12.91</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.52</td>
    <td align="right">1.48</td>
    <td align="right">1.49</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.80</td>
    <td align="right">1.55</td>
    <td align="right">1.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.48</td>
    <td align="right">9.40</td>
    <td align="right">12.16</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.80</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.85</td>
    <td align="right">1.72</td>
    <td align="right">1.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.90</td>
    <td align="right">12.33</td>
    <td align="right">12.65</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.97</td>
    <td align="right">1.92</td>
    <td align="right">2.11</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.95</td>
    <td align="right">1.62</td>
    <td align="right">1.76</td>
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
    <td align="right">2.33</td>
    <td align="right">1.84</td>
    <td align="right">1.88</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.50</td>
    <td align="right">2.31</td>
    <td align="right">1.89</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.17</td>
    <td align="right">1.86</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.36</td>
    <td align="right">2.27</td>
    <td align="right">2.27</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.99</td>
    <td align="right">2.47</td>
    <td align="right">2.37</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.56</td>
    <td align="right">2.10</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.39</td>
    <td align="right">3.06</td>
    <td align="right">3.01</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.25</td>
    <td align="right">3.73</td>
    <td align="right">3.35</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.16</td>
    <td align="right">2.40</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.63</td>
    <td align="right">3.51</td>
    <td align="right">5.76</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.35</td>
    <td align="right">4.24</td>
    <td align="right">3.97</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.00</td>
    <td align="right">2.93</td>
    <td align="right">2.87</td>
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
    <td align="right">2.18</td>
    <td align="right">1.93</td>
    <td align="right">1.91</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.29</td>
    <td align="right">1.84</td>
    <td align="right">1.91</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.35</td>
    <td align="right">1.93</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.21</td>
    <td align="right">1.74</td>
    <td align="right">1.76</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.42</td>
    <td align="right">2.32</td>
    <td align="right">2.27</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.07</td>
    <td align="right">2.42</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.96</td>
    <td align="right">2.77</td>
    <td align="right">2.02</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.61</td>
    <td align="right">3.28</td>
    <td align="right">3.28</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.53</td>
    <td align="right">3.22</td>
    <td align="right">3.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.36</td>
    <td align="right">3.53</td>
    <td align="right">2.01</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.25</td>
    <td align="right">4.08</td>
    <td align="right">3.71</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.39</td>
    <td align="right">4.45</td>
    <td align="right">4.54</td>
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
    <td align="right">3.60</td>
    <td align="right">8.56</td>
    <td align="right">8.44</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">5.87</td>
    <td align="right">10.07</td>
    <td align="right">10.07</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.91</td>
    <td align="right">10.18</td>
    <td align="right">9.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">5.92</td>
    <td align="right">9.68</td>
    <td align="right">9.47</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">5.19</td>
    <td align="right">9.44</td>
    <td align="right">9.83</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">9.03</td>
    <td align="right">9.63</td>
    <td align="right">8.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">7.83</td>
    <td align="right">13.60</td>
    <td align="right">11.54</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">9.40</td>
    <td align="right">11.16</td>
    <td align="right">10.27</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">12.69</td>
    <td align="right">15.53</td>
    <td align="right">12.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.01</td>
    <td align="right">17.03</td>
    <td align="right">16.32</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">11.16</td>
    <td align="right">13.79</td>
    <td align="right">15.16</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">16.17</td>
    <td align="right">14.05</td>
    <td align="right">15.55</td>
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
    <td align="right">37.39</td>
    <td align="right">22.46</td>
    <td align="right">10.56</td>
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
    <td align="right">15.94</td>
    <td align="right">15.66</td>
    <td align="right">25.06</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.41</td>
    <td align="right">4.99</td>
    <td align="right">7.39</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.81</td>
    <td align="right">6.55</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">53.72</td>
    <td align="right">44.09</td>
    <td align="right">33.35</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">13.08</td>
    <td align="right">9.70</td>
    <td align="right">8.95</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.29</td>
    <td align="right">7.95</td>
    <td align="right">11.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">68.27</td>
    <td align="right">52.41</td>
    <td align="right">28.47</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">13.28</td>
    <td align="right">10.25</td>
    <td align="right">10.87</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">13.16</td>
    <td align="right">10.51</td>
    <td align="right">10.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">87.58</td>
    <td align="right">86.07</td>
    <td align="right">36.53</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.40</td>
    <td align="right">16.75</td>
    <td align="right">14.57</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">15.39</td>
    <td align="right">14.96</td>
    <td align="right">14.52</td>
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
    <td align="right">6.93</td>
    <td align="right">9.08</td>
    <td align="right">11.02</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.55</td>
    <td align="right">10.05</td>
    <td align="right">7.02</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">7.56</td>
    <td align="right">9.48</td>
    <td align="right">10.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.51</td>
    <td align="right">12.63</td>
    <td align="right">13.85</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">13.57</td>
    <td align="right">12.72</td>
    <td align="right">13.62</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">8.36</td>
    <td align="right">7.50</td>
    <td align="right">7.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">17.16</td>
    <td align="right">12.81</td>
    <td align="right">12.52</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.59</td>
    <td align="right">9.26</td>
    <td align="right">9.03</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.44</td>
    <td align="right">9.51</td>
    <td align="right">5.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.34</td>
    <td align="right">12.27</td>
    <td align="right">13.81</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.17</td>
    <td align="right">15.10</td>
    <td align="right">16.61</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.24</td>
    <td align="right">11.00</td>
    <td align="right">6.13</td>
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
    <td align="right">2.59</td>
    <td align="right">2.72</td>
    <td align="right">2.74</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.85</td>
    <td align="right">2.53</td>
    <td align="right">2.67</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.98</td>
    <td align="right">2.80</td>
    <td align="right">2.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">4.83</td>
    <td align="right">3.11</td>
    <td align="right">3.51</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.59</td>
    <td align="right">4.87</td>
    <td align="right">4.01</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">5.07</td>
    <td align="right">5.81</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.84</td>
    <td align="right">8.17</td>
    <td align="right">5.42</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.13</td>
    <td align="right">12.16</td>
    <td align="right">10.03</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.59</td>
    <td align="right">9.50</td>
    <td align="right">9.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.53</td>
    <td align="right">11.10</td>
    <td align="right">5.99</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.61</td>
    <td align="right">12.32</td>
    <td align="right">12.28</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.54</td>
    <td align="right">13.31</td>
    <td align="right">13.25</td>
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
    <td align="right">4.78</td>
    <td align="right">7.94</td>
    <td align="right">8.24</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">6.85</td>
    <td align="right">7.88</td>
    <td align="right">7.95</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">8.75</td>
    <td align="right">8.27</td>
    <td align="right">8.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">8.88</td>
    <td align="right">11.04</td>
    <td align="right">11.32</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.14</td>
    <td align="right">9.99</td>
    <td align="right">9.99</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.19</td>
    <td align="right">9.93</td>
    <td align="right">10.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">15.60</td>
    <td align="right">15.21</td>
    <td align="right">15.26</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">15.28</td>
    <td align="right">15.52</td>
    <td align="right">15.09</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">20.83</td>
    <td align="right">16.54</td>
    <td align="right">16.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">21.54</td>
    <td align="right">22.42</td>
    <td align="right">22.36</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">19.90</td>
    <td align="right">19.39</td>
    <td align="right">20.47</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">27.30</td>
    <td align="right">21.65</td>
    <td align="right">21.74</td>
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
    <td align="right">35.21</td>
    <td align="right">5.84</td>
    <td align="right">3.59</td>
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
    <td align="right">12.21</td>
    <td align="right">12.48</td>
    <td align="right">16.95</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.87</td>
    <td align="right">4.27</td>
    <td align="right">4.29</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">7.05</td>
    <td align="right">5.32</td>
    <td align="right">5.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.54</td>
    <td align="right">17.72</td>
    <td align="right">17.75</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.97</td>
    <td align="right">4.75</td>
    <td align="right">4.96</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.06</td>
    <td align="right">5.92</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.56</td>
    <td align="right">21.31</td>
    <td align="right">16.60</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.59</td>
    <td align="right">5.35</td>
    <td align="right">5.34</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.30</td>
    <td align="right">6.57</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.12</td>
    <td align="right">27.49</td>
    <td align="right">17.37</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.97</td>
    <td align="right">5.95</td>
    <td align="right">6.02</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.45</td>
    <td align="right">7.53</td>
    <td align="right">7.38</td>
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
    <td align="right">7.97</td>
    <td align="right">5.57</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.19</td>
    <td align="right">5.69</td>
    <td align="right">5.69</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.48</td>
    <td align="right">3.98</td>
    <td align="right">3.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.16</td>
    <td align="right">8.19</td>
    <td align="right">8.23</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.46</td>
    <td align="right">8.75</td>
    <td align="right">8.78</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.93</td>
    <td align="right">4.91</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.61</td>
    <td align="right">10.93</td>
    <td align="right">11.03</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.97</td>
    <td align="right">10.46</td>
    <td align="right">10.44</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.07</td>
    <td align="right">7.17</td>
    <td align="right">5.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.17</td>
    <td align="right">15.13</td>
    <td align="right">14.70</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.56</td>
    <td align="right">13.79</td>
    <td align="right">12.82</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.20</td>
    <td align="right">7.23</td>
    <td align="right">5.49</td>
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
    <td align="right">3.31</td>
    <td align="right">3.83</td>
    <td align="right">3.90</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.53</td>
    <td align="right">5.49</td>
    <td align="right">5.47</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.71</td>
    <td align="right">5.35</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.42</td>
    <td align="right">5.59</td>
    <td align="right">5.37</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.83</td>
    <td align="right">5.94</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">7.07</td>
    <td align="right">7.01</td>
    <td align="right">6.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.12</td>
    <td align="right">6.84</td>
    <td align="right">5.05</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.96</td>
    <td align="right">9.34</td>
    <td align="right">7.67</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.93</td>
    <td align="right">9.40</td>
    <td align="right">7.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.21</td>
    <td align="right">7.06</td>
    <td align="right">5.24</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.38</td>
    <td align="right">10.66</td>
    <td align="right">7.75</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.43</td>
    <td align="right">10.69</td>
    <td align="right">7.56</td>
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
    <td align="right">8.67</td>
    <td align="right">16.22</td>
    <td align="right">16.22</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.95</td>
    <td align="right">23.99</td>
    <td align="right">23.85</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.72</td>
    <td align="right">24.09</td>
    <td align="right">23.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.74</td>
    <td align="right">18.00</td>
    <td align="right">17.95</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">12.48</td>
    <td align="right">23.05</td>
    <td align="right">22.95</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">14.03</td>
    <td align="right">24.88</td>
    <td align="right">24.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.19</td>
    <td align="right">19.28</td>
    <td align="right">19.26</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">15.22</td>
    <td align="right">22.65</td>
    <td align="right">22.61</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">18.40</td>
    <td align="right">28.48</td>
    <td align="right">28.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">18.50</td>
    <td align="right">20.26</td>
    <td align="right">20.25</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">18.97</td>
    <td align="right">21.36</td>
    <td align="right">21.37</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">21.93</td>
    <td align="right">31.02</td>
    <td align="right">31.18</td>
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
    <td align="right">45.84</td>
    <td align="right">21.88</td>
    <td align="right">10.13</td>
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
    <td align="right">14.62</td>
    <td align="right">13.07</td>
    <td align="right">17.62</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.08</td>
    <td align="right">4.55</td>
    <td align="right">4.56</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.90</td>
    <td align="right">5.59</td>
    <td align="right">5.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">27.32</td>
    <td align="right">27.25</td>
    <td align="right">20.38</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.01</td>
    <td align="right">5.24</td>
    <td align="right">5.16</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.19</td>
    <td align="right">11.56</td>
    <td align="right">10.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">38.05</td>
    <td align="right">44.47</td>
    <td align="right">24.18</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.37</td>
    <td align="right">11.42</td>
    <td align="right">11.76</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">17.12</td>
    <td align="right">13.77</td>
    <td align="right">17.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">92.49</td>
    <td align="right">87.07</td>
    <td align="right">26.54</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">22.91</td>
    <td align="right">19.97</td>
    <td align="right">18.67</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">27.22</td>
    <td align="right">24.28</td>
    <td align="right">24.59</td>
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
    <td align="right">10.18</td>
    <td align="right">7.12</td>
    <td align="right">6.81</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">13.42</td>
    <td align="right">6.41</td>
    <td align="right">6.67</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.99</td>
    <td align="right">4.33</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">25.22</td>
    <td align="right">17.38</td>
    <td align="right">22.12</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">17.56</td>
    <td align="right">9.82</td>
    <td align="right">9.79</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.29</td>
    <td align="right">10.72</td>
    <td align="right">6.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">31.46</td>
    <td align="right">26.02</td>
    <td align="right">29.63</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">39.68</td>
    <td align="right">27.71</td>
    <td align="right">27.65</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">17.26</td>
    <td align="right">23.23</td>
    <td align="right">18.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">40.80</td>
    <td align="right">33.25</td>
    <td align="right">34.01</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">48.79</td>
    <td align="right">37.42</td>
    <td align="right">39.68</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">18.34</td>
    <td align="right">24.29</td>
    <td align="right">18.82</td>
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
    <td align="right">3.73</td>
    <td align="right">4.36</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.35</td>
    <td align="right">7.93</td>
    <td align="right">6.56</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.54</td>
    <td align="right">6.54</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">5.40</td>
    <td align="right">12.36</td>
    <td align="right">8.68</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">15.40</td>
    <td align="right">17.13</td>
    <td align="right">15.73</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">22.13</td>
    <td align="right">20.24</td>
    <td align="right">18.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">17.28</td>
    <td align="right">23.32</td>
    <td align="right">17.34</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.52</td>
    <td align="right">18.64</td>
    <td align="right">13.40</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">18.68</td>
    <td align="right">18.28</td>
    <td align="right">15.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">18.25</td>
    <td align="right">24.60</td>
    <td align="right">16.65</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">29.38</td>
    <td align="right">36.96</td>
    <td align="right">22.90</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">26.39</td>
    <td align="right">30.39</td>
    <td align="right">19.11</td>
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
    <td align="right">17.31</td>
    <td align="right">17.41</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">10.06</td>
    <td align="right">24.45</td>
    <td align="right">24.26</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.63</td>
    <td align="right">25.84</td>
    <td align="right">25.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">20.41</td>
    <td align="right">24.64</td>
    <td align="right">20.06</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">15.28</td>
    <td align="right">25.88</td>
    <td align="right">25.49</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">16.31</td>
    <td align="right">30.22</td>
    <td align="right">32.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">19.67</td>
    <td align="right">23.65</td>
    <td align="right">26.13</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">23.27</td>
    <td align="right">27.93</td>
    <td align="right">28.43</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">29.28</td>
    <td align="right">51.94</td>
    <td align="right">55.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">45.99</td>
    <td align="right">41.31</td>
    <td align="right">39.07</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">36.83</td>
    <td align="right">41.45</td>
    <td align="right">38.91</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">51.13</td>
    <td align="right">72.02</td>
    <td align="right">85.25</td>
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
    <td align="right">60.95</td>
    <td align="right">32.53</td>
    <td align="right">16.80</td>
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
    <td align="right">27.38</td>
    <td align="right">42.11</td>
    <td align="right">36.50</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.55</td>
    <td align="right">15.57</td>
    <td align="right">15.52</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.19</td>
    <td align="right">19.05</td>
    <td align="right">19.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.14</td>
    <td align="right">60.33</td>
    <td align="right">37.55</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.34</td>
    <td align="right">19.79</td>
    <td align="right">19.51</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.24</td>
    <td align="right">18.65</td>
    <td align="right">18.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.93</td>
    <td align="right">78.28</td>
    <td align="right">38.25</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.42</td>
    <td align="right">18.53</td>
    <td align="right">18.45</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.18</td>
    <td align="right">18.26</td>
    <td align="right">18.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.67</td>
    <td align="right">97.73</td>
    <td align="right">38.00</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.18</td>
    <td align="right">18.70</td>
    <td align="right">18.71</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.03</td>
    <td align="right">19.92</td>
    <td align="right">19.94</td>
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
    <td align="right">16.22</td>
    <td align="right">21.18</td>
    <td align="right">21.18</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.70</td>
    <td align="right">22.15</td>
    <td align="right">22.16</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.99</td>
    <td align="right">13.65</td>
    <td align="right">13.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.02</td>
    <td align="right">26.04</td>
    <td align="right">26.06</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.77</td>
    <td align="right">27.80</td>
    <td align="right">27.78</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.98</td>
    <td align="right">15.83</td>
    <td align="right">15.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.29</td>
    <td align="right">33.01</td>
    <td align="right">33.03</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.53</td>
    <td align="right">46.63</td>
    <td align="right">46.85</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">15.12</td>
    <td align="right">19.56</td>
    <td align="right">19.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.37</td>
    <td align="right">36.15</td>
    <td align="right">36.19</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.64</td>
    <td align="right">56.40</td>
    <td align="right">56.41</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.33</td>
    <td align="right">25.60</td>
    <td align="right">25.54</td>
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
    <td align="right">15.51</td>
    <td align="right">15.60</td>
    <td align="right">15.61</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.22</td>
    <td align="right">21.26</td>
    <td align="right">21.22</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.75</td>
    <td align="right">22.16</td>
    <td align="right">22.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">20.09</td>
    <td align="right">20.45</td>
    <td align="right">20.41</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.01</td>
    <td align="right">26.05</td>
    <td align="right">26.02</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.83</td>
    <td align="right">27.78</td>
    <td align="right">27.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.57</td>
    <td align="right">24.76</td>
    <td align="right">24.78</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.33</td>
    <td align="right">33.13</td>
    <td align="right">33.01</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.50</td>
    <td align="right">46.60</td>
    <td align="right">46.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.54</td>
    <td align="right">37.35</td>
    <td align="right">37.36</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.45</td>
    <td align="right">36.17</td>
    <td align="right">36.17</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.60</td>
    <td align="right">56.42</td>
    <td align="right">56.39</td>
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
    <td align="right">12.88</td>
    <td align="right">31.60</td>
    <td align="right">31.61</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.22</td>
    <td align="right">28.43</td>
    <td align="right">28.43</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.37</td>
    <td align="right">48.61</td>
    <td align="right">48.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">20.70</td>
    <td align="right">37.91</td>
    <td align="right">39.40</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.14</td>
    <td align="right">41.27</td>
    <td align="right">41.18</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.65</td>
    <td align="right">58.05</td>
    <td align="right">58.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">23.78</td>
    <td align="right">41.62</td>
    <td align="right">41.12</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.74</td>
    <td align="right">43.99</td>
    <td align="right">43.96</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">47.23</td>
    <td align="right">69.80</td>
    <td align="right">69.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">27.62</td>
    <td align="right">46.60</td>
    <td align="right">46.41</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.62</td>
    <td align="right">50.00</td>
    <td align="right">49.98</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">48.71</td>
    <td align="right">71.05</td>
    <td align="right">71.12</td>
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
    <td align="right">68.74</td>
    <td align="right">103.54</td>
    <td align="right">20.86</td>
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
    <td align="right">27.34</td>
    <td align="right">42.47</td>
    <td align="right">39.21</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.75</td>
    <td align="right">15.49</td>
    <td align="right">15.51</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.25</td>
    <td align="right">19.15</td>
    <td align="right">19.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.40</td>
    <td align="right">61.82</td>
    <td align="right">40.47</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.30</td>
    <td align="right">19.77</td>
    <td align="right">19.79</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.13</td>
    <td align="right">18.78</td>
    <td align="right">18.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">43.20</td>
    <td align="right">74.92</td>
    <td align="right">38.45</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.09</td>
    <td align="right">18.48</td>
    <td align="right">18.32</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">17.90</td>
    <td align="right">18.19</td>
    <td align="right">19.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">84.54</td>
    <td align="right">97.70</td>
    <td align="right">39.59</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">19.74</td>
    <td align="right">21.61</td>
    <td align="right">21.78</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">31.89</td>
    <td align="right">25.91</td>
    <td align="right">28.27</td>
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
    <td align="right">17.37</td>
    <td align="right">22.69</td>
    <td align="right">22.08</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">76.38</td>
    <td align="right">53.49</td>
    <td align="right">50.00</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">19.59</td>
    <td align="right">29.66</td>
    <td align="right">28.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">55.39</td>
    <td align="right">61.74</td>
    <td align="right">58.54</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">115.80</td>
    <td align="right">87.29</td>
    <td align="right">88.45</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">35.97</td>
    <td align="right">42.52</td>
    <td align="right">39.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">94.32</td>
    <td align="right">103.76</td>
    <td align="right">99.52</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">138.80</td>
    <td align="right">109.16</td>
    <td align="right">105.72</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">56.78</td>
    <td align="right">58.53</td>
    <td align="right">60.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">116.33</td>
    <td align="right">115.49</td>
    <td align="right">119.09</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">149.69</td>
    <td align="right">125.15</td>
    <td align="right">125.54</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">69.80</td>
    <td align="right">94.36</td>
    <td align="right">96.98</td>
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
    <td align="right">32.08</td>
    <td align="right">28.92</td>
    <td align="right">29.55</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">38.48</td>
    <td align="right">49.67</td>
    <td align="right">46.59</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">90.95</td>
    <td align="right">53.64</td>
    <td align="right">53.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">58.69</td>
    <td align="right">58.90</td>
    <td align="right">61.14</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">61.63</td>
    <td align="right">63.31</td>
    <td align="right">64.21</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">130.75</td>
    <td align="right">102.68</td>
    <td align="right">103.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">114.12</td>
    <td align="right">70.23</td>
    <td align="right">70.11</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">104.55</td>
    <td align="right">107.43</td>
    <td align="right">119.21</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">138.07</td>
    <td align="right">52.99</td>
    <td align="right">60.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">128.64</td>
    <td align="right">129.18</td>
    <td align="right">132.73</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">117.12</td>
    <td align="right">125.72</td>
    <td align="right">126.95</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">118.18</td>
    <td align="right">78.02</td>
    <td align="right">149.12</td>
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
    <td align="right">30.05</td>
    <td align="right">90.62</td>
    <td align="right">102.16</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">51.55</td>
    <td align="right">99.36</td>
    <td align="right">92.61</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">115.42</td>
    <td align="right">129.15</td>
    <td align="right">132.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">62.67</td>
    <td align="right">108.07</td>
    <td align="right">54.03</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">29.06</td>
    <td align="right">54.13</td>
    <td align="right">57.41</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">127.27</td>
    <td align="right">148.73</td>
    <td align="right">145.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">23.70</td>
    <td align="right">42.77</td>
    <td align="right">43.68</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">32.99</td>
    <td align="right">43.84</td>
    <td align="right">43.91</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">47.23</td>
    <td align="right">70.73</td>
    <td align="right">70.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">27.72</td>
    <td align="right">47.47</td>
    <td align="right">48.64</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">38.23</td>
    <td align="right">54.33</td>
    <td align="right">66.94</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">64.66</td>
    <td align="right">84.33</td>
    <td align="right">70.67</td>
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
    <td align="right">64.93</td>
    <td align="right">11.06</td>
    <td align="right">8.80</td>
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
    <td align="right">14.20</td>
    <td align="right">23.32</td>
    <td align="right">26.78</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.75</td>
    <td align="right">12.64</td>
    <td align="right">12.55</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">12.01</td>
    <td align="right">13.97</td>
    <td align="right">14.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.90</td>
    <td align="right">35.38</td>
    <td align="right">28.93</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.13</td>
    <td align="right">14.45</td>
    <td align="right">14.49</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.55</td>
    <td align="right">15.49</td>
    <td align="right">15.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.45</td>
    <td align="right">47.42</td>
    <td align="right">30.33</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.84</td>
    <td align="right">15.46</td>
    <td align="right">15.44</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.75</td>
    <td align="right">16.93</td>
    <td align="right">16.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">29.88</td>
    <td align="right">59.93</td>
    <td align="right">29.52</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.09</td>
    <td align="right">15.69</td>
    <td align="right">15.58</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.30</td>
    <td align="right">17.10</td>
    <td align="right">17.09</td>
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
    <td align="right">12.76</td>
    <td align="right">16.15</td>
    <td align="right">16.14</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.33</td>
    <td align="right">16.80</td>
    <td align="right">16.98</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.29</td>
    <td align="right">9.70</td>
    <td align="right">9.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.77</td>
    <td align="right">22.75</td>
    <td align="right">22.68</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.75</td>
    <td align="right">22.73</td>
    <td align="right">22.73</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.36</td>
    <td align="right">14.41</td>
    <td align="right">14.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.39</td>
    <td align="right">32.64</td>
    <td align="right">32.71</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.98</td>
    <td align="right">31.35</td>
    <td align="right">31.28</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.29</td>
    <td align="right">17.81</td>
    <td align="right">17.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.34</td>
    <td align="right">34.54</td>
    <td align="right">34.57</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.82</td>
    <td align="right">34.33</td>
    <td align="right">34.60</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">15.56</td>
    <td align="right">19.21</td>
    <td align="right">19.27</td>
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
    <td align="right">6.84</td>
    <td align="right">9.59</td>
    <td align="right">9.61</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">13.19</td>
    <td align="right">16.36</td>
    <td align="right">16.47</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.51</td>
    <td align="right">17.10</td>
    <td align="right">16.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">11.07</td>
    <td align="right">13.89</td>
    <td align="right">13.89</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.59</td>
    <td align="right">22.65</td>
    <td align="right">22.74</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.65</td>
    <td align="right">22.53</td>
    <td align="right">22.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.02</td>
    <td align="right">17.86</td>
    <td align="right">17.87</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.34</td>
    <td align="right">32.77</td>
    <td align="right">32.73</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">26.29</td>
    <td align="right">31.17</td>
    <td align="right">31.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">15.46</td>
    <td align="right">19.55</td>
    <td align="right">19.45</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.33</td>
    <td align="right">34.42</td>
    <td align="right">34.39</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.58</td>
    <td align="right">34.46</td>
    <td align="right">34.32</td>
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
    <td align="right">11.75</td>
    <td align="right">32.09</td>
    <td align="right">32.46</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.82</td>
    <td align="right">28.10</td>
    <td align="right">28.32</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">51.27</td>
    <td align="right">37.22</td>
    <td align="right">37.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">14.88</td>
    <td align="right">33.48</td>
    <td align="right">33.54</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.94</td>
    <td align="right">35.53</td>
    <td align="right">35.23</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">53.51</td>
    <td align="right">52.28</td>
    <td align="right">52.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">18.05</td>
    <td align="right">33.96</td>
    <td align="right">34.49</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.17</td>
    <td align="right">39.40</td>
    <td align="right">39.15</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">60.09</td>
    <td align="right">58.91</td>
    <td align="right">58.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">19.32</td>
    <td align="right">34.87</td>
    <td align="right">34.84</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">28.57</td>
    <td align="right">41.83</td>
    <td align="right">41.80</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">63.25</td>
    <td align="right">54.04</td>
    <td align="right">54.24</td>
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
    <td align="right">92.16</td>
    <td align="right">52.41</td>
    <td align="right">14.22</td>
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
    <td align="right">14.65</td>
    <td align="right">23.33</td>
    <td align="right">28.85</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.97</td>
    <td align="right">13.19</td>
    <td align="right">13.22</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.30</td>
    <td align="right">15.02</td>
    <td align="right">14.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.45</td>
    <td align="right">34.51</td>
    <td align="right">30.39</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.98</td>
    <td align="right">14.34</td>
    <td align="right">15.04</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.69</td>
    <td align="right">15.42</td>
    <td align="right">15.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">29.30</td>
    <td align="right">58.82</td>
    <td align="right">36.28</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.20</td>
    <td align="right">17.67</td>
    <td align="right">16.29</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">15.29</td>
    <td align="right">19.53</td>
    <td align="right">16.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">48.74</td>
    <td align="right">77.96</td>
    <td align="right">36.51</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">20.81</td>
    <td align="right">20.87</td>
    <td align="right">19.63</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">22.75</td>
    <td align="right">23.07</td>
    <td align="right">23.64</td>
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
    <td align="right">13.07</td>
    <td align="right">16.72</td>
    <td align="right">16.71</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.36</td>
    <td align="right">17.54</td>
    <td align="right">17.52</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.32</td>
    <td align="right">9.50</td>
    <td align="right">9.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.92</td>
    <td align="right">22.80</td>
    <td align="right">22.36</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">19.44</td>
    <td align="right">23.80</td>
    <td align="right">22.09</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">10.74</td>
    <td align="right">13.85</td>
    <td align="right">14.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.65</td>
    <td align="right">57.97</td>
    <td align="right">51.70</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">46.21</td>
    <td align="right">43.58</td>
    <td align="right">37.12</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.12</td>
    <td align="right">18.12</td>
    <td align="right">22.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">31.79</td>
    <td align="right">57.93</td>
    <td align="right">57.66</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">58.28</td>
    <td align="right">56.76</td>
    <td align="right">51.39</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">31.55</td>
    <td align="right">45.39</td>
    <td align="right">55.51</td>
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
    <td align="right">6.80</td>
    <td align="right">9.67</td>
    <td align="right">9.65</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.15</td>
    <td align="right">16.68</td>
    <td align="right">16.69</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.44</td>
    <td align="right">19.37</td>
    <td align="right">20.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">13.30</td>
    <td align="right">13.97</td>
    <td align="right">15.06</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.28</td>
    <td align="right">22.77</td>
    <td align="right">24.34</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">26.55</td>
    <td align="right">24.36</td>
    <td align="right">26.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">15.01</td>
    <td align="right">22.90</td>
    <td align="right">20.03</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.89</td>
    <td align="right">43.69</td>
    <td align="right">43.34</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">38.42</td>
    <td align="right">35.80</td>
    <td align="right">51.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">45.08</td>
    <td align="right">40.00</td>
    <td align="right">33.25</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">32.96</td>
    <td align="right">37.15</td>
    <td align="right">39.01</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">36.50</td>
    <td align="right">46.63</td>
    <td align="right">39.75</td>
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
    <td align="right">12.47</td>
    <td align="right">28.42</td>
    <td align="right">28.41</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">13.53</td>
    <td align="right">28.12</td>
    <td align="right">28.83</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">49.30</td>
    <td align="right">39.30</td>
    <td align="right">39.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">14.63</td>
    <td align="right">31.83</td>
    <td align="right">31.84</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">19.87</td>
    <td align="right">35.06</td>
    <td align="right">34.65</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">53.02</td>
    <td align="right">54.30</td>
    <td align="right">52.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">17.95</td>
    <td align="right">35.88</td>
    <td align="right">36.99</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.54</td>
    <td align="right">39.44</td>
    <td align="right">39.37</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">70.82</td>
    <td align="right">78.34</td>
    <td align="right">101.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">38.10</td>
    <td align="right">48.70</td>
    <td align="right">56.26</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">58.38</td>
    <td align="right">77.24</td>
    <td align="right">99.05</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">121.58</td>
    <td align="right">59.83</td>
    <td align="right">69.78</td>
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
    <td align="right">42.20</td>
    <td align="right">8.50</td>
    <td align="right">6.56</td>
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
    <td align="right">60.11</td>
    <td align="right">59.08</td>
    <td align="right">44.33</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.76</td>
    <td align="right">23.32</td>
    <td align="right">26.42</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.11</td>
    <td align="right">26.28</td>
    <td align="right">29.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.58</td>
    <td align="right">85.13</td>
    <td align="right">46.63</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">24.13</td>
    <td align="right">24.29</td>
    <td align="right">26.23</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">26.85</td>
    <td align="right">28.34</td>
    <td align="right">30.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.32</td>
    <td align="right">101.90</td>
    <td align="right">46.45</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.17</td>
    <td align="right">25.18</td>
    <td align="right">26.38</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.58</td>
    <td align="right">30.92</td>
    <td align="right">31.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">139.95</td>
    <td align="right">126.87</td>
    <td align="right">47.17</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.23</td>
    <td align="right">26.95</td>
    <td align="right">27.85</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">30.96</td>
    <td align="right">33.46</td>
    <td align="right">32.95</td>
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
    <td align="right">23.63</td>
    <td align="right">43.05</td>
    <td align="right">43.05</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.10</td>
    <td align="right">43.46</td>
    <td align="right">43.46</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.59</td>
    <td align="right">24.80</td>
    <td align="right">25.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.19</td>
    <td align="right">58.56</td>
    <td align="right">58.81</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.69</td>
    <td align="right">59.83</td>
    <td align="right">59.71</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.55</td>
    <td align="right">36.40</td>
    <td align="right">25.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.11</td>
    <td align="right">79.84</td>
    <td align="right">80.65</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.84</td>
    <td align="right">81.01</td>
    <td align="right">80.68</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">28.92</td>
    <td align="right">54.87</td>
    <td align="right">39.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.17</td>
    <td align="right">88.71</td>
    <td align="right">88.57</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.24</td>
    <td align="right">96.27</td>
    <td align="right">95.84</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.11</td>
    <td align="right">55.63</td>
    <td align="right">40.35</td>
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
    <td align="right">18.58</td>
    <td align="right">26.29</td>
    <td align="right">26.25</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.75</td>
    <td align="right">29.16</td>
    <td align="right">29.29</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.91</td>
    <td align="right">31.09</td>
    <td align="right">31.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.14</td>
    <td align="right">46.84</td>
    <td align="right">35.11</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.43</td>
    <td align="right">40.65</td>
    <td align="right">27.61</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">20.94</td>
    <td align="right">51.84</td>
    <td align="right">40.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.70</td>
    <td align="right">54.38</td>
    <td align="right">39.24</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">32.99</td>
    <td align="right">52.69</td>
    <td align="right">35.32</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.03</td>
    <td align="right">61.19</td>
    <td align="right">44.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.77</td>
    <td align="right">55.45</td>
    <td align="right">39.36</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.70</td>
    <td align="right">64.12</td>
    <td align="right">44.19</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.19</td>
    <td align="right">64.14</td>
    <td align="right">44.48</td>
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
    <td align="right">23.60</td>
    <td align="right">26.76</td>
    <td align="right">26.96</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.32</td>
    <td align="right">32.62</td>
    <td align="right">53.66</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.95</td>
    <td align="right">42.20</td>
    <td align="right">61.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">33.68</td>
    <td align="right">35.90</td>
    <td align="right">35.71</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">35.91</td>
    <td align="right">43.70</td>
    <td align="right">74.07</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">42.28</td>
    <td align="right">53.97</td>
    <td align="right">82.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">37.90</td>
    <td align="right">38.52</td>
    <td align="right">39.70</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">41.42</td>
    <td align="right">44.65</td>
    <td align="right">75.69</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.20</td>
    <td align="right">59.82</td>
    <td align="right">90.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">46.11</td>
    <td align="right">46.06</td>
    <td align="right">45.49</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">51.67</td>
    <td align="right">56.11</td>
    <td align="right">93.00</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">57.66</td>
    <td align="right">69.60</td>
    <td align="right">104.41</td>
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
    <td align="right">60.57</td>
    <td align="right">37.19</td>
    <td align="right">12.12</td>
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
    <td align="right">66.88</td>
    <td align="right">63.81</td>
    <td align="right">48.58</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.58</td>
    <td align="right">23.61</td>
    <td align="right">28.15</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">27.92</td>
    <td align="right">29.07</td>
    <td align="right">33.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">107.30</td>
    <td align="right">101.69</td>
    <td align="right">53.01</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">27.25</td>
    <td align="right">25.50</td>
    <td align="right">29.55</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">31.44</td>
    <td align="right">31.62</td>
    <td align="right">34.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">142.21</td>
    <td align="right">132.24</td>
    <td align="right">54.16</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">33.88</td>
    <td align="right">28.57</td>
    <td align="right">29.48</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">37.24</td>
    <td align="right">37.97</td>
    <td align="right">38.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">225.21</td>
    <td align="right">214.91</td>
    <td align="right">63.52</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">40.99</td>
    <td align="right">38.38</td>
    <td align="right">38.21</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">51.45</td>
    <td align="right">47.68</td>
    <td align="right">47.02</td>
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
    <td align="right">25.55</td>
    <td align="right">43.77</td>
    <td align="right">43.90</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">30.59</td>
    <td align="right">44.95</td>
    <td align="right">44.64</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">19.98</td>
    <td align="right">30.91</td>
    <td align="right">31.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">31.39</td>
    <td align="right">60.18</td>
    <td align="right">60.73</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">38.85</td>
    <td align="right">63.34</td>
    <td align="right">64.02</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.65</td>
    <td align="right">40.45</td>
    <td align="right">29.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">45.45</td>
    <td align="right">84.75</td>
    <td align="right">84.94</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">54.16</td>
    <td align="right">88.50</td>
    <td align="right">87.51</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">39.52</td>
    <td align="right">79.85</td>
    <td align="right">62.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">55.58</td>
    <td align="right">105.37</td>
    <td align="right">97.49</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">66.91</td>
    <td align="right">108.98</td>
    <td align="right">109.45</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">46.28</td>
    <td align="right">85.08</td>
    <td align="right">70.50</td>
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
    <td align="right">19.86</td>
    <td align="right">31.46</td>
    <td align="right">31.29</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">22.20</td>
    <td align="right">34.61</td>
    <td align="right">35.45</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">22.02</td>
    <td align="right">39.63</td>
    <td align="right">36.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.47</td>
    <td align="right">63.30</td>
    <td align="right">43.43</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.38</td>
    <td align="right">45.35</td>
    <td align="right">35.42</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">25.89</td>
    <td align="right">81.28</td>
    <td align="right">67.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">57.68</td>
    <td align="right">86.99</td>
    <td align="right">83.33</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">41.08</td>
    <td align="right">70.88</td>
    <td align="right">51.29</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">55.89</td>
    <td align="right">75.99</td>
    <td align="right">53.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">49.44</td>
    <td align="right">80.90</td>
    <td align="right">83.88</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">56.99</td>
    <td align="right">100.25</td>
    <td align="right">80.12</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">62.90</td>
    <td align="right">114.97</td>
    <td align="right">85.78</td>
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
    <td align="right">27.91</td>
    <td align="right">31.13</td>
    <td align="right">33.13</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">44.44</td>
    <td align="right">34.90</td>
    <td align="right">74.84</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">67.63</td>
    <td align="right">65.79</td>
    <td align="right">80.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">50.72</td>
    <td align="right">52.87</td>
    <td align="right">49.33</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">61.27</td>
    <td align="right">60.53</td>
    <td align="right">98.82</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">69.60</td>
    <td align="right">92.53</td>
    <td align="right">126.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">76.72</td>
    <td align="right">54.97</td>
    <td align="right">61.75</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">74.33</td>
    <td align="right">64.02</td>
    <td align="right">104.68</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">97.06</td>
    <td align="right">103.29</td>
    <td align="right">150.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">116.90</td>
    <td align="right">68.88</td>
    <td align="right">67.17</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">102.14</td>
    <td align="right">78.67</td>
    <td align="right">122.63</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">123.49</td>
    <td align="right">140.03</td>
    <td align="right">175.23</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
