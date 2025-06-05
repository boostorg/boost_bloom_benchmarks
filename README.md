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
    <td align="right">26.10</td>
    <td align="right">4.60</td>
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
    <td align="right">11.22</td>
    <td align="right">10.63</td>
    <td align="right">16.64</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.05</td>
    <td align="right">4.39</td>
    <td align="right">4.40</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.89</td>
    <td align="right">5.12</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.87</td>
    <td align="right">15.67</td>
    <td align="right">17.74</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.84</td>
    <td align="right">4.96</td>
    <td align="right">4.99</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.46</td>
    <td align="right">5.54</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.22</td>
    <td align="right">18.86</td>
    <td align="right">16.54</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.45</td>
    <td align="right">5.34</td>
    <td align="right">5.35</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.29</td>
    <td align="right">6.33</td>
    <td align="right">6.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.74</td>
    <td align="right">23.43</td>
    <td align="right">16.83</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.23</td>
    <td align="right">5.95</td>
    <td align="right">5.96</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.74</td>
    <td align="right">6.62</td>
    <td align="right">6.63</td>
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
    <td align="right">5.74</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.29</td>
    <td align="right">6.64</td>
    <td align="right">6.53</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.98</td>
    <td align="right">3.30</td>
    <td align="right">3.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.53</td>
    <td align="right">8.85</td>
    <td align="right">8.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.22</td>
    <td align="right">9.89</td>
    <td align="right">9.88</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.48</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.22</td>
    <td align="right">13.23</td>
    <td align="right">13.17</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.60</td>
    <td align="right">15.01</td>
    <td align="right">15.00</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.78</td>
    <td align="right">5.79</td>
    <td align="right">3.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.12</td>
    <td align="right">14.89</td>
    <td align="right">14.89</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.24</td>
    <td align="right">16.19</td>
    <td align="right">16.22</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.80</td>
    <td align="right">5.82</td>
    <td align="right">3.94</td>
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
    <td align="right">2.95</td>
    <td align="right">3.29</td>
    <td align="right">3.25</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.41</td>
    <td align="right">5.12</td>
    <td align="right">5.06</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.57</td>
    <td align="right">5.05</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.06</td>
    <td align="right">3.35</td>
    <td align="right">3.32</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.21</td>
    <td align="right">4.47</td>
    <td align="right">4.47</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.44</td>
    <td align="right">5.13</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.43</td>
    <td align="right">5.53</td>
    <td align="right">3.79</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.07</td>
    <td align="right">7.73</td>
    <td align="right">5.95</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.96</td>
    <td align="right">7.66</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.47</td>
    <td align="right">5.51</td>
    <td align="right">3.84</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.04</td>
    <td align="right">9.11</td>
    <td align="right">5.99</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.32</td>
    <td align="right">9.05</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">6.92</td>
    <td align="right">7.03</td>
    <td align="right">13.61</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.53</td>
    <td align="right">8.97</td>
    <td align="right">17.42</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.82</td>
    <td align="right">11.06</td>
    <td align="right">11.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.43</td>
    <td align="right">8.20</td>
    <td align="right">12.46</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.32</td>
    <td align="right">9.56</td>
    <td align="right">14.29</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">15.71</td>
    <td align="right">16.04</td>
    <td align="right">16.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.00</td>
    <td align="right">10.38</td>
    <td align="right">12.04</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.51</td>
    <td align="right">12.73</td>
    <td align="right">15.28</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">19.14</td>
    <td align="right">19.12</td>
    <td align="right">19.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.55</td>
    <td align="right">12.80</td>
    <td align="right">13.18</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.99</td>
    <td align="right">14.22</td>
    <td align="right">14.90</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">25.90</td>
    <td align="right">26.69</td>
    <td align="right">26.48</td>
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
    <td align="right">31.08</td>
    <td align="right">17.87</td>
    <td align="right">6.92</td>
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
    <td align="right">14.15</td>
    <td align="right">13.32</td>
    <td align="right">17.93</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.84</td>
    <td align="right">5.16</td>
    <td align="right">5.14</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.85</td>
    <td align="right">6.07</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">20.13</td>
    <td align="right">19.11</td>
    <td align="right">18.81</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.77</td>
    <td align="right">5.93</td>
    <td align="right">5.71</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.26</td>
    <td align="right">6.29</td>
    <td align="right">6.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">25.63</td>
    <td align="right">25.14</td>
    <td align="right">17.31</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.42</td>
    <td align="right">7.16</td>
    <td align="right">9.10</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.27</td>
    <td align="right">8.22</td>
    <td align="right">8.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">55.16</td>
    <td align="right">49.69</td>
    <td align="right">20.32</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.30</td>
    <td align="right">10.47</td>
    <td align="right">12.04</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.71</td>
    <td align="right">11.87</td>
    <td align="right">11.47</td>
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
    <td align="right">6.11</td>
    <td align="right">6.94</td>
    <td align="right">6.91</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.28</td>
    <td align="right">7.94</td>
    <td align="right">7.89</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.62</td>
    <td align="right">4.13</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.52</td>
    <td align="right">9.85</td>
    <td align="right">10.06</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.45</td>
    <td align="right">11.49</td>
    <td align="right">11.68</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.03</td>
    <td align="right">3.80</td>
    <td align="right">3.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.96</td>
    <td align="right">15.87</td>
    <td align="right">16.62</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.83</td>
    <td align="right">18.92</td>
    <td align="right">23.19</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.21</td>
    <td align="right">8.25</td>
    <td align="right">5.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.78</td>
    <td align="right">21.18</td>
    <td align="right">20.85</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.38</td>
    <td align="right">22.87</td>
    <td align="right">24.02</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.96</td>
    <td align="right">10.23</td>
    <td align="right">6.66</td>
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
    <td align="right">3.61</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.28</td>
    <td align="right">6.21</td>
    <td align="right">6.13</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.40</td>
    <td align="right">6.07</td>
    <td align="right">6.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.57</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.82</td>
    <td align="right">5.50</td>
    <td align="right">5.22</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">5.10</td>
    <td align="right">6.04</td>
    <td align="right">6.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.34</td>
    <td align="right">7.88</td>
    <td align="right">5.22</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.93</td>
    <td align="right">10.74</td>
    <td align="right">7.51</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.91</td>
    <td align="right">10.10</td>
    <td align="right">8.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.26</td>
    <td align="right">10.06</td>
    <td align="right">8.16</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">12.73</td>
    <td align="right">17.02</td>
    <td align="right">11.29</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.61</td>
    <td align="right">16.97</td>
    <td align="right">11.89</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">8.33</td>
    <td align="right">8.42</td>
    <td align="right">14.24</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.87</td>
    <td align="right">10.44</td>
    <td align="right">18.23</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">14.67</td>
    <td align="right">14.34</td>
    <td align="right">14.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.13</td>
    <td align="right">9.55</td>
    <td align="right">12.94</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">14.29</td>
    <td align="right">10.74</td>
    <td align="right">14.90</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">22.99</td>
    <td align="right">22.79</td>
    <td align="right">22.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">14.96</td>
    <td align="right">14.27</td>
    <td align="right">13.76</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">20.25</td>
    <td align="right">16.50</td>
    <td align="right">17.06</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">25.76</td>
    <td align="right">25.78</td>
    <td align="right">25.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">24.97</td>
    <td align="right">20.96</td>
    <td align="right">16.45</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">32.47</td>
    <td align="right">25.51</td>
    <td align="right">18.79</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">37.31</td>
    <td align="right">36.23</td>
    <td align="right">36.65</td>
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
    <td align="right">26.58</td>
    <td align="right">4.20</td>
    <td align="right">3.34</td>
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
    <td align="right">9.39</td>
    <td align="right">9.01</td>
    <td align="right">15.41</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.69</td>
    <td align="right">4.01</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.84</td>
    <td align="right">4.71</td>
    <td align="right">4.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.18</td>
    <td align="right">13.48</td>
    <td align="right">16.57</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.11</td>
    <td align="right">4.64</td>
    <td align="right">4.59</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.42</td>
    <td align="right">5.27</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.51</td>
    <td align="right">16.97</td>
    <td align="right">15.59</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.54</td>
    <td align="right">5.10</td>
    <td align="right">5.28</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.60</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.05</td>
    <td align="right">22.41</td>
    <td align="right">15.91</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.59</td>
    <td align="right">5.71</td>
    <td align="right">5.89</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.90</td>
    <td align="right">3.34</td>
    <td align="right">3.35</td>
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
    <td align="right">3.09</td>
    <td align="right">3.61</td>
    <td align="right">3.61</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.19</td>
    <td align="right">3.59</td>
    <td align="right">3.54</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.62</td>
    <td align="right">2.55</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.75</td>
    <td align="right">4.11</td>
    <td align="right">4.12</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.78</td>
    <td align="right">4.41</td>
    <td align="right">4.49</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.16</td>
    <td align="right">2.29</td>
    <td align="right">2.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.64</td>
    <td align="right">7.23</td>
    <td align="right">7.22</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.78</td>
    <td align="right">7.04</td>
    <td align="right">7.06</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.23</td>
    <td align="right">4.41</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.02</td>
    <td align="right">7.61</td>
    <td align="right">7.63</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.39</td>
    <td align="right">8.20</td>
    <td align="right">8.18</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.23</td>
    <td align="right">4.49</td>
    <td align="right">3.18</td>
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
    <td align="right">2.62</td>
    <td align="right">2.37</td>
    <td align="right">2.38</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.67</td>
    <td align="right">4.09</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.71</td>
    <td align="right">3.95</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.77</td>
    <td align="right">2.46</td>
    <td align="right">2.45</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.96</td>
    <td align="right">3.76</td>
    <td align="right">3.79</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.91</td>
    <td align="right">4.08</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.28</td>
    <td align="right">4.35</td>
    <td align="right">2.99</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.72</td>
    <td align="right">6.10</td>
    <td align="right">4.70</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.86</td>
    <td align="right">6.09</td>
    <td align="right">4.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.32</td>
    <td align="right">4.36</td>
    <td align="right">2.99</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.73</td>
    <td align="right">7.29</td>
    <td align="right">4.98</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.01</td>
    <td align="right">7.18</td>
    <td align="right">4.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">6.89</td>
    <td align="right">6.13</td>
    <td align="right">12.21</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.48</td>
    <td align="right">8.07</td>
    <td align="right">16.42</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.98</td>
    <td align="right">11.43</td>
    <td align="right">11.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.54</td>
    <td align="right">8.23</td>
    <td align="right">12.21</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.70</td>
    <td align="right">9.65</td>
    <td align="right">13.95</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">16.41</td>
    <td align="right">16.80</td>
    <td align="right">17.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.71</td>
    <td align="right">10.01</td>
    <td align="right">11.81</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.05</td>
    <td align="right">12.50</td>
    <td align="right">14.75</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">19.36</td>
    <td align="right">19.53</td>
    <td align="right">19.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.99</td>
    <td align="right">12.37</td>
    <td align="right">12.69</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.96</td>
    <td align="right">13.95</td>
    <td align="right">14.29</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">26.35</td>
    <td align="right">26.23</td>
    <td align="right">25.09</td>
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
    <td align="right">33.33</td>
    <td align="right">17.91</td>
    <td align="right">6.52</td>
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
    <td align="right">10.71</td>
    <td align="right">10.12</td>
    <td align="right">15.96</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.45</td>
    <td align="right">4.27</td>
    <td align="right">4.40</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.60</td>
    <td align="right">5.08</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">14.62</td>
    <td align="right">14.85</td>
    <td align="right">16.82</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.55</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">8.94</td>
    <td align="right">5.59</td>
    <td align="right">5.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">21.45</td>
    <td align="right">21.47</td>
    <td align="right">16.47</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.63</td>
    <td align="right">6.27</td>
    <td align="right">6.55</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.69</td>
    <td align="right">7.29</td>
    <td align="right">7.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">34.90</td>
    <td align="right">36.67</td>
    <td align="right">18.16</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.71</td>
    <td align="right">9.10</td>
    <td align="right">8.96</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.53</td>
    <td align="right">5.33</td>
    <td align="right">5.14</td>
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
    <td align="right">3.46</td>
    <td align="right">4.00</td>
    <td align="right">4.00</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.59</td>
    <td align="right">3.91</td>
    <td align="right">3.91</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.92</td>
    <td align="right">2.88</td>
    <td align="right">2.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.98</td>
    <td align="right">4.43</td>
    <td align="right">4.44</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.03</td>
    <td align="right">4.68</td>
    <td align="right">4.79</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.43</td>
    <td align="right">2.51</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">7.01</td>
    <td align="right">8.66</td>
    <td align="right">8.78</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.06</td>
    <td align="right">8.69</td>
    <td align="right">8.72</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.11</td>
    <td align="right">5.60</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.56</td>
    <td align="right">10.84</td>
    <td align="right">10.90</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">8.74</td>
    <td align="right">11.56</td>
    <td align="right">11.54</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.21</td>
    <td align="right">7.63</td>
    <td align="right">5.45</td>
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
    <td align="right">2.96</td>
    <td align="right">2.69</td>
    <td align="right">2.70</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.11</td>
    <td align="right">4.50</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.14</td>
    <td align="right">4.33</td>
    <td align="right">4.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.97</td>
    <td align="right">2.78</td>
    <td align="right">2.72</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.17</td>
    <td align="right">4.00</td>
    <td align="right">3.99</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.19</td>
    <td align="right">4.37</td>
    <td align="right">4.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">4.40</td>
    <td align="right">4.36</td>
    <td align="right">3.00</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.54</td>
    <td align="right">7.12</td>
    <td align="right">6.75</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">6.96</td>
    <td align="right">7.49</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">6.82</td>
    <td align="right">7.30</td>
    <td align="right">5.12</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">9.29</td>
    <td align="right">10.22</td>
    <td align="right">7.35</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">8.93</td>
    <td align="right">9.35</td>
    <td align="right">7.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">7.54</td>
    <td align="right">6.66</td>
    <td align="right">12.40</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.68</td>
    <td align="right">8.47</td>
    <td align="right">16.72</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">16.53</td>
    <td align="right">16.88</td>
    <td align="right">16.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">9.82</td>
    <td align="right">8.49</td>
    <td align="right">12.32</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.32</td>
    <td align="right">10.90</td>
    <td align="right">14.95</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">21.26</td>
    <td align="right">21.32</td>
    <td align="right">21.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">13.98</td>
    <td align="right">11.83</td>
    <td align="right">12.94</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">17.86</td>
    <td align="right">15.06</td>
    <td align="right">15.82</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">24.95</td>
    <td align="right">25.05</td>
    <td align="right">24.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">21.19</td>
    <td align="right">17.19</td>
    <td align="right">15.02</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">29.42</td>
    <td align="right">23.73</td>
    <td align="right">19.25</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">36.35</td>
    <td align="right">35.07</td>
    <td align="right">34.10</td>
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
    <td align="right">24.44</td>
    <td align="right">4.17</td>
    <td align="right">2.66</td>
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
    <td align="right">7.07</td>
    <td align="right">4.94</td>
    <td align="right">13.04</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.37</td>
    <td align="right">1.25</td>
    <td align="right">1.37</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.72</td>
    <td align="right">1.38</td>
    <td align="right">1.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.19</td>
    <td align="right">7.76</td>
    <td align="right">12.93</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.45</td>
    <td align="right">1.51</td>
    <td align="right">1.46</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.87</td>
    <td align="right">1.60</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.69</td>
    <td align="right">9.73</td>
    <td align="right">12.82</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.91</td>
    <td align="right">1.95</td>
    <td align="right">3.06</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.44</td>
    <td align="right">2.11</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.38</td>
    <td align="right">13.68</td>
    <td align="right">21.17</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.85</td>
    <td align="right">2.67</td>
    <td align="right">3.56</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.50</td>
    <td align="right">2.40</td>
    <td align="right">2.23</td>
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
    <td align="right">2.67</td>
    <td align="right">2.04</td>
    <td align="right">2.35</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.70</td>
    <td align="right">2.04</td>
    <td align="right">1.97</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.29</td>
    <td align="right">2.18</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.60</td>
    <td align="right">2.26</td>
    <td align="right">2.55</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.30</td>
    <td align="right">2.93</td>
    <td align="right">2.62</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.85</td>
    <td align="right">2.24</td>
    <td align="right">2.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">7.58</td>
    <td align="right">4.54</td>
    <td align="right">3.25</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">7.55</td>
    <td align="right">3.71</td>
    <td align="right">3.36</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.37</td>
    <td align="right">2.91</td>
    <td align="right">2.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.93</td>
    <td align="right">5.00</td>
    <td align="right">4.29</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.38</td>
    <td align="right">4.80</td>
    <td align="right">4.59</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.97</td>
    <td align="right">3.62</td>
    <td align="right">2.54</td>
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
    <td align="right">2.12</td>
    <td align="right">1.89</td>
    <td align="right">2.00</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.49</td>
    <td align="right">1.94</td>
    <td align="right">2.18</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.51</td>
    <td align="right">2.80</td>
    <td align="right">5.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.23</td>
    <td align="right">2.52</td>
    <td align="right">1.76</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.49</td>
    <td align="right">2.39</td>
    <td align="right">2.34</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.47</td>
    <td align="right">2.83</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.33</td>
    <td align="right">2.84</td>
    <td align="right">2.04</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.68</td>
    <td align="right">3.28</td>
    <td align="right">3.64</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.62</td>
    <td align="right">3.45</td>
    <td align="right">3.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.43</td>
    <td align="right">3.59</td>
    <td align="right">2.31</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.92</td>
    <td align="right">4.60</td>
    <td align="right">4.24</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">8.73</td>
    <td align="right">5.74</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">3.89</td>
    <td align="right">4.84</td>
    <td align="right">14.99</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">9.25</td>
    <td align="right">5.02</td>
    <td align="right">15.64</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">11.94</td>
    <td align="right">5.95</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">5.42</td>
    <td align="right">5.73</td>
    <td align="right">12.47</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">11.58</td>
    <td align="right">5.89</td>
    <td align="right">13.25</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">11.99</td>
    <td align="right">8.04</td>
    <td align="right">7.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">7.39</td>
    <td align="right">6.73</td>
    <td align="right">12.62</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">11.62</td>
    <td align="right">7.29</td>
    <td align="right">13.21</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">13.83</td>
    <td align="right">9.55</td>
    <td align="right">9.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">9.68</td>
    <td align="right">8.70</td>
    <td align="right">13.31</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">13.07</td>
    <td align="right">8.76</td>
    <td align="right">12.90</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">20.32</td>
    <td align="right">13.47</td>
    <td align="right">13.30</td>
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
    <td align="right">36.69</td>
    <td align="right">17.50</td>
    <td align="right">11.93</td>
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
    <td align="right">12.46</td>
    <td align="right">12.20</td>
    <td align="right">21.65</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.66</td>
    <td align="right">5.48</td>
    <td align="right">5.13</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.84</td>
    <td align="right">4.74</td>
    <td align="right">4.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">41.54</td>
    <td align="right">30.57</td>
    <td align="right">28.35</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">12.67</td>
    <td align="right">9.12</td>
    <td align="right">9.24</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.25</td>
    <td align="right">8.74</td>
    <td align="right">9.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">64.27</td>
    <td align="right">48.48</td>
    <td align="right">29.81</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.67</td>
    <td align="right">10.85</td>
    <td align="right">10.69</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.47</td>
    <td align="right">12.51</td>
    <td align="right">15.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">102.19</td>
    <td align="right">69.42</td>
    <td align="right">29.36</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.76</td>
    <td align="right">14.29</td>
    <td align="right">14.36</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">14.79</td>
    <td align="right">11.14</td>
    <td align="right">13.78</td>
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
    <td align="right">5.84</td>
    <td align="right">6.84</td>
    <td align="right">6.79</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.32</td>
    <td align="right">6.13</td>
    <td align="right">5.36</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">6.01</td>
    <td align="right">7.87</td>
    <td align="right">6.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.35</td>
    <td align="right">11.48</td>
    <td align="right">9.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.22</td>
    <td align="right">10.06</td>
    <td align="right">11.61</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">9.51</td>
    <td align="right">9.05</td>
    <td align="right">9.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">21.90</td>
    <td align="right">17.76</td>
    <td align="right">18.00</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">26.30</td>
    <td align="right">19.05</td>
    <td align="right">16.75</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">15.42</td>
    <td align="right">17.05</td>
    <td align="right">10.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">26.51</td>
    <td align="right">20.57</td>
    <td align="right">20.36</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.01</td>
    <td align="right">24.13</td>
    <td align="right">21.61</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.28</td>
    <td align="right">15.28</td>
    <td align="right">9.29</td>
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
    <td align="right">4.54</td>
    <td align="right">6.55</td>
    <td align="right">5.01</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.31</td>
    <td align="right">6.54</td>
    <td align="right">6.60</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.30</td>
    <td align="right">7.26</td>
    <td align="right">7.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">9.83</td>
    <td align="right">9.96</td>
    <td align="right">12.11</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.94</td>
    <td align="right">14.68</td>
    <td align="right">13.63</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.77</td>
    <td align="right">13.51</td>
    <td align="right">14.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">17.82</td>
    <td align="right">16.33</td>
    <td align="right">10.32</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">24.53</td>
    <td align="right">21.43</td>
    <td align="right">20.80</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">26.24</td>
    <td align="right">20.97</td>
    <td align="right">24.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">19.95</td>
    <td align="right">19.30</td>
    <td align="right">12.26</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">28.84</td>
    <td align="right">23.79</td>
    <td align="right">26.52</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">31.80</td>
    <td align="right">28.27</td>
    <td align="right">28.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">18.55</td>
    <td align="right">13.96</td>
    <td align="right">24.91</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">24.08</td>
    <td align="right">12.60</td>
    <td align="right">25.00</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">27.10</td>
    <td align="right">25.33</td>
    <td align="right">26.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">29.17</td>
    <td align="right">26.86</td>
    <td align="right">22.22</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">47.85</td>
    <td align="right">28.40</td>
    <td align="right">28.08</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">51.82</td>
    <td align="right">52.11</td>
    <td align="right">53.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">34.78</td>
    <td align="right">29.79</td>
    <td align="right">21.36</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">61.68</td>
    <td align="right">41.84</td>
    <td align="right">27.53</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">63.31</td>
    <td align="right">59.45</td>
    <td align="right">59.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">46.54</td>
    <td align="right">44.10</td>
    <td align="right">26.29</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">78.44</td>
    <td align="right">45.21</td>
    <td align="right">30.09</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">96.49</td>
    <td align="right">82.20</td>
    <td align="right">82.36</td>
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
    <td align="right">34.83</td>
    <td align="right">5.74</td>
    <td align="right">3.48</td>
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
    <td align="right">12.05</td>
    <td align="right">12.55</td>
    <td align="right">16.98</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.82</td>
    <td align="right">4.37</td>
    <td align="right">4.26</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.93</td>
    <td align="right">5.26</td>
    <td align="right">5.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.32</td>
    <td align="right">17.72</td>
    <td align="right">17.66</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.96</td>
    <td align="right">4.79</td>
    <td align="right">4.79</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.00</td>
    <td align="right">5.94</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.64</td>
    <td align="right">21.65</td>
    <td align="right">16.61</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.61</td>
    <td align="right">5.35</td>
    <td align="right">5.36</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.30</td>
    <td align="right">6.74</td>
    <td align="right">6.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.83</td>
    <td align="right">27.41</td>
    <td align="right">17.52</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.87</td>
    <td align="right">5.99</td>
    <td align="right">5.93</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.35</td>
    <td align="right">7.49</td>
    <td align="right">7.42</td>
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
    <td align="right">7.86</td>
    <td align="right">5.64</td>
    <td align="right">5.55</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.17</td>
    <td align="right">5.70</td>
    <td align="right">5.58</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.38</td>
    <td align="right">3.95</td>
    <td align="right">3.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.64</td>
    <td align="right">8.14</td>
    <td align="right">8.17</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.22</td>
    <td align="right">8.73</td>
    <td align="right">7.86</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.93</td>
    <td align="right">4.90</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.07</td>
    <td align="right">11.14</td>
    <td align="right">10.86</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">23.68</td>
    <td align="right">10.88</td>
    <td align="right">10.44</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.04</td>
    <td align="right">7.09</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">16.87</td>
    <td align="right">12.52</td>
    <td align="right">12.57</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">22.74</td>
    <td align="right">13.41</td>
    <td align="right">13.44</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.18</td>
    <td align="right">7.12</td>
    <td align="right">5.31</td>
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
    <td align="right">3.25</td>
    <td align="right">3.86</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.50</td>
    <td align="right">5.48</td>
    <td align="right">5.56</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.65</td>
    <td align="right">5.37</td>
    <td align="right">5.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.37</td>
    <td align="right">5.52</td>
    <td align="right">4.64</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.84</td>
    <td align="right">5.81</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.94</td>
    <td align="right">7.16</td>
    <td align="right">6.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.08</td>
    <td align="right">6.82</td>
    <td align="right">5.05</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.91</td>
    <td align="right">9.41</td>
    <td align="right">7.69</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.71</td>
    <td align="right">9.34</td>
    <td align="right">7.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.13</td>
    <td align="right">6.87</td>
    <td align="right">5.05</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.34</td>
    <td align="right">10.90</td>
    <td align="right">7.78</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.19</td>
    <td align="right">10.44</td>
    <td align="right">7.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">8.60</td>
    <td align="right">8.66</td>
    <td align="right">13.72</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.16</td>
    <td align="right">11.60</td>
    <td align="right">17.08</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">12.91</td>
    <td align="right">10.61</td>
    <td align="right">10.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.83</td>
    <td align="right">11.07</td>
    <td align="right">13.01</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.36</td>
    <td align="right">13.08</td>
    <td align="right">14.43</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">17.86</td>
    <td align="right">16.65</td>
    <td align="right">16.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.56</td>
    <td align="right">14.06</td>
    <td align="right">12.73</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">19.40</td>
    <td align="right">17.50</td>
    <td align="right">15.33</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">21.62</td>
    <td align="right">18.55</td>
    <td align="right">19.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.42</td>
    <td align="right">17.66</td>
    <td align="right">13.97</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">20.74</td>
    <td align="right">20.66</td>
    <td align="right">14.86</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">29.42</td>
    <td align="right">28.40</td>
    <td align="right">27.20</td>
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
    <td align="right">41.73</td>
    <td align="right">21.50</td>
    <td align="right">8.26</td>
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
    <td align="right">14.52</td>
    <td align="right">13.26</td>
    <td align="right">17.69</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.03</td>
    <td align="right">4.49</td>
    <td align="right">4.54</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.01</td>
    <td align="right">5.58</td>
    <td align="right">5.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.48</td>
    <td align="right">19.24</td>
    <td align="right">18.75</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.64</td>
    <td align="right">5.10</td>
    <td align="right">5.19</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.41</td>
    <td align="right">6.37</td>
    <td align="right">6.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">32.04</td>
    <td align="right">28.51</td>
    <td align="right">18.38</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.75</td>
    <td align="right">6.64</td>
    <td align="right">6.28</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.01</td>
    <td align="right">7.63</td>
    <td align="right">8.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">54.74</td>
    <td align="right">55.10</td>
    <td align="right">21.24</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.37</td>
    <td align="right">9.02</td>
    <td align="right">9.16</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">14.90</td>
    <td align="right">11.97</td>
    <td align="right">11.31</td>
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
    <td align="right">9.31</td>
    <td align="right">6.24</td>
    <td align="right">6.25</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.62</td>
    <td align="right">6.30</td>
    <td align="right">6.34</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.84</td>
    <td align="right">4.23</td>
    <td align="right">4.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.39</td>
    <td align="right">9.60</td>
    <td align="right">9.59</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.06</td>
    <td align="right">9.36</td>
    <td align="right">8.74</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.19</td>
    <td align="right">5.29</td>
    <td align="right">4.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.76</td>
    <td align="right">15.28</td>
    <td align="right">14.96</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">26.35</td>
    <td align="right">12.31</td>
    <td align="right">12.25</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.26</td>
    <td align="right">9.84</td>
    <td align="right">6.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">21.33</td>
    <td align="right">17.48</td>
    <td align="right">17.44</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">29.27</td>
    <td align="right">18.29</td>
    <td align="right">18.87</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.17</td>
    <td align="right">12.01</td>
    <td align="right">9.32</td>
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
    <td align="right">3.57</td>
    <td align="right">4.39</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.83</td>
    <td align="right">6.21</td>
    <td align="right">6.92</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.33</td>
    <td align="right">5.99</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">4.75</td>
    <td align="right">7.82</td>
    <td align="right">5.75</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">7.47</td>
    <td align="right">7.58</td>
    <td align="right">6.01</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.79</td>
    <td align="right">7.98</td>
    <td align="right">7.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.96</td>
    <td align="right">12.07</td>
    <td align="right">7.06</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">12.02</td>
    <td align="right">10.64</td>
    <td align="right">8.69</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">11.16</td>
    <td align="right">10.80</td>
    <td align="right">8.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.89</td>
    <td align="right">12.54</td>
    <td align="right">9.56</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">17.19</td>
    <td align="right">19.02</td>
    <td align="right">13.60</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.27</td>
    <td align="right">14.38</td>
    <td align="right">10.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">9.76</td>
    <td align="right">9.76</td>
    <td align="right">14.09</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.74</td>
    <td align="right">12.73</td>
    <td align="right">17.73</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">17.13</td>
    <td align="right">15.95</td>
    <td align="right">15.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">14.09</td>
    <td align="right">12.37</td>
    <td align="right">13.67</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">15.14</td>
    <td align="right">14.46</td>
    <td align="right">15.20</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">21.83</td>
    <td align="right">21.26</td>
    <td align="right">20.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.85</td>
    <td align="right">17.52</td>
    <td align="right">14.20</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">25.18</td>
    <td align="right">22.60</td>
    <td align="right">16.62</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">27.54</td>
    <td align="right">22.49</td>
    <td align="right">23.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">28.90</td>
    <td align="right">27.20</td>
    <td align="right">17.20</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">35.97</td>
    <td align="right">37.21</td>
    <td align="right">18.91</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">39.45</td>
    <td align="right">36.66</td>
    <td align="right">37.13</td>
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
    <td align="right">62.40</td>
    <td align="right">32.91</td>
    <td align="right">17.26</td>
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
    <td align="right">27.61</td>
    <td align="right">41.72</td>
    <td align="right">35.92</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.48</td>
    <td align="right">15.49</td>
    <td align="right">15.49</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.22</td>
    <td align="right">19.21</td>
    <td align="right">19.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.98</td>
    <td align="right">63.59</td>
    <td align="right">40.54</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.33</td>
    <td align="right">19.52</td>
    <td align="right">19.51</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.20</td>
    <td align="right">18.59</td>
    <td align="right">18.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.00</td>
    <td align="right">78.29</td>
    <td align="right">38.59</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.43</td>
    <td align="right">18.43</td>
    <td align="right">18.53</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.11</td>
    <td align="right">18.30</td>
    <td align="right">18.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">53.03</td>
    <td align="right">90.00</td>
    <td align="right">34.94</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">17.44</td>
    <td align="right">18.57</td>
    <td align="right">18.58</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.17</td>
    <td align="right">19.55</td>
    <td align="right">19.59</td>
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
    <td align="right">21.25</td>
    <td align="right">21.23</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.68</td>
    <td align="right">22.20</td>
    <td align="right">22.18</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.97</td>
    <td align="right">13.61</td>
    <td align="right">13.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.38</td>
    <td align="right">26.07</td>
    <td align="right">26.02</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.71</td>
    <td align="right">27.71</td>
    <td align="right">27.74</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">13.06</td>
    <td align="right">16.32</td>
    <td align="right">15.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.13</td>
    <td align="right">33.12</td>
    <td align="right">33.12</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.61</td>
    <td align="right">46.57</td>
    <td align="right">46.88</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.99</td>
    <td align="right">19.54</td>
    <td align="right">19.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">33.14</td>
    <td align="right">34.09</td>
    <td align="right">34.13</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">76.25</td>
    <td align="right">55.24</td>
    <td align="right">55.23</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">21.64</td>
    <td align="right">23.92</td>
    <td align="right">23.91</td>
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
    <td align="right">15.36</td>
    <td align="right">15.58</td>
    <td align="right">15.61</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.20</td>
    <td align="right">21.18</td>
    <td align="right">21.20</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.69</td>
    <td align="right">22.19</td>
    <td align="right">22.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.80</td>
    <td align="right">20.44</td>
    <td align="right">20.42</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.31</td>
    <td align="right">25.99</td>
    <td align="right">25.99</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.66</td>
    <td align="right">27.77</td>
    <td align="right">27.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.47</td>
    <td align="right">24.74</td>
    <td align="right">24.51</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.05</td>
    <td align="right">33.07</td>
    <td align="right">33.07</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.59</td>
    <td align="right">46.61</td>
    <td align="right">46.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">33.47</td>
    <td align="right">35.28</td>
    <td align="right">35.28</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">33.06</td>
    <td align="right">34.04</td>
    <td align="right">34.08</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">76.18</td>
    <td align="right">55.16</td>
    <td align="right">55.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">17.20</td>
    <td align="right">20.80</td>
    <td align="right">25.55</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.35</td>
    <td align="right">29.15</td>
    <td align="right">34.62</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">27.66</td>
    <td align="right">30.12</td>
    <td align="right">30.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.19</td>
    <td align="right">28.24</td>
    <td align="right">26.23</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.94</td>
    <td align="right">33.34</td>
    <td align="right">30.48</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">37.99</td>
    <td align="right">38.48</td>
    <td align="right">38.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.66</td>
    <td align="right">33.74</td>
    <td align="right">25.62</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">46.99</td>
    <td align="right">41.85</td>
    <td align="right">33.41</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.88</td>
    <td align="right">41.63</td>
    <td align="right">41.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">36.22</td>
    <td align="right">38.52</td>
    <td align="right">25.82</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">46.98</td>
    <td align="right">42.01</td>
    <td align="right">30.09</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">53.79</td>
    <td align="right">58.33</td>
    <td align="right">58.23</td>
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
    <td align="right">76.93</td>
    <td align="right">109.89</td>
    <td align="right">22.62</td>
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
    <td align="right">28.69</td>
    <td align="right">44.08</td>
    <td align="right">39.88</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.06</td>
    <td align="right">16.05</td>
    <td align="right">15.96</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.75</td>
    <td align="right">19.37</td>
    <td align="right">19.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">37.80</td>
    <td align="right">68.74</td>
    <td align="right">44.19</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">18.79</td>
    <td align="right">21.27</td>
    <td align="right">21.30</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">17.85</td>
    <td align="right">20.65</td>
    <td align="right">22.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">54.72</td>
    <td align="right">91.90</td>
    <td align="right">45.47</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">22.81</td>
    <td align="right">23.33</td>
    <td align="right">25.54</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">25.90</td>
    <td align="right">23.81</td>
    <td align="right">26.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">106.33</td>
    <td align="right">162.84</td>
    <td align="right">54.94</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">33.78</td>
    <td align="right">30.68</td>
    <td align="right">37.09</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">36.74</td>
    <td align="right">36.97</td>
    <td align="right">37.40</td>
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
    <td align="right">17.18</td>
    <td align="right">23.02</td>
    <td align="right">22.80</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">35.03</td>
    <td align="right">23.70</td>
    <td align="right">23.98</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.37</td>
    <td align="right">14.62</td>
    <td align="right">14.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.99</td>
    <td align="right">28.17</td>
    <td align="right">27.86</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">50.53</td>
    <td align="right">36.73</td>
    <td align="right">33.19</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">13.66</td>
    <td align="right">17.57</td>
    <td align="right">16.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">41.55</td>
    <td align="right">49.18</td>
    <td align="right">47.77</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">72.75</td>
    <td align="right">58.73</td>
    <td align="right">68.06</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">22.89</td>
    <td align="right">27.51</td>
    <td align="right">26.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">54.72</td>
    <td align="right">61.10</td>
    <td align="right">64.15</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">99.93</td>
    <td align="right">71.26</td>
    <td align="right">71.16</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">48.20</td>
    <td align="right">60.81</td>
    <td align="right">54.28</td>
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
    <td align="right">16.42</td>
    <td align="right">16.43</td>
    <td align="right">16.44</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.13</td>
    <td align="right">22.56</td>
    <td align="right">22.43</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">35.24</td>
    <td align="right">23.77</td>
    <td align="right">23.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">21.52</td>
    <td align="right">23.39</td>
    <td align="right">22.49</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">23.06</td>
    <td align="right">28.11</td>
    <td align="right">27.28</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">49.96</td>
    <td align="right">32.47</td>
    <td align="right">32.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">42.86</td>
    <td align="right">35.82</td>
    <td align="right">37.19</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">38.87</td>
    <td align="right">50.18</td>
    <td align="right">50.08</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">72.11</td>
    <td align="right">55.26</td>
    <td align="right">65.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">83.98</td>
    <td align="right">88.96</td>
    <td align="right">80.10</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">52.96</td>
    <td align="right">58.82</td>
    <td align="right">64.10</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">101.39</td>
    <td align="right">73.96</td>
    <td align="right">71.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">17.78</td>
    <td align="right">21.68</td>
    <td align="right">26.67</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">33.81</td>
    <td align="right">30.48</td>
    <td align="right">37.16</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">29.70</td>
    <td align="right">32.70</td>
    <td align="right">32.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">29.61</td>
    <td align="right">33.62</td>
    <td align="right">28.32</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">47.59</td>
    <td align="right">40.30</td>
    <td align="right">34.64</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">39.43</td>
    <td align="right">40.35</td>
    <td align="right">40.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">47.60</td>
    <td align="right">53.21</td>
    <td align="right">32.90</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">77.06</td>
    <td align="right">68.75</td>
    <td align="right">45.46</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">43.83</td>
    <td align="right">44.79</td>
    <td align="right">45.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">61.63</td>
    <td align="right">67.24</td>
    <td align="right">38.98</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">94.05</td>
    <td align="right">90.63</td>
    <td align="right">53.11</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">66.87</td>
    <td align="right">80.02</td>
    <td align="right">73.33</td>
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
    <td align="right">65.23</td>
    <td align="right">10.81</td>
    <td align="right">8.28</td>
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
    <td align="right">14.27</td>
    <td align="right">23.16</td>
    <td align="right">26.80</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">10.37</td>
    <td align="right">12.34</td>
    <td align="right">12.32</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">28.87</td>
    <td align="right">14.02</td>
    <td align="right">13.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.94</td>
    <td align="right">35.42</td>
    <td align="right">29.27</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">31.24</td>
    <td align="right">14.12</td>
    <td align="right">14.18</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">14.74</td>
    <td align="right">15.37</td>
    <td align="right">15.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.47</td>
    <td align="right">47.64</td>
    <td align="right">29.47</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">14.79</td>
    <td align="right">15.35</td>
    <td align="right">15.33</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">16.33</td>
    <td align="right">16.75</td>
    <td align="right">16.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.71</td>
    <td align="right">61.09</td>
    <td align="right">31.05</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">16.20</td>
    <td align="right">16.26</td>
    <td align="right">16.27</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">17.35</td>
    <td align="right">17.90</td>
    <td align="right">17.85</td>
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
    <td align="right">12.71</td>
    <td align="right">16.11</td>
    <td align="right">16.15</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.25</td>
    <td align="right">16.70</td>
    <td align="right">16.69</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">6.99</td>
    <td align="right">9.35</td>
    <td align="right">9.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.40</td>
    <td align="right">22.40</td>
    <td align="right">22.50</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.89</td>
    <td align="right">22.52</td>
    <td align="right">22.51</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">10.88</td>
    <td align="right">14.24</td>
    <td align="right">14.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.26</td>
    <td align="right">32.20</td>
    <td align="right">32.19</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.83</td>
    <td align="right">30.97</td>
    <td align="right">30.96</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.60</td>
    <td align="right">17.57</td>
    <td align="right">17.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.11</td>
    <td align="right">35.64</td>
    <td align="right">35.68</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.98</td>
    <td align="right">35.94</td>
    <td align="right">35.83</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.25</td>
    <td align="right">20.51</td>
    <td align="right">20.56</td>
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
    <td align="right">6.63</td>
    <td align="right">9.38</td>
    <td align="right">9.36</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.69</td>
    <td align="right">16.10</td>
    <td align="right">16.08</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.26</td>
    <td align="right">16.70</td>
    <td align="right">16.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">11.76</td>
    <td align="right">13.81</td>
    <td align="right">13.70</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.41</td>
    <td align="right">22.45</td>
    <td align="right">22.52</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.96</td>
    <td align="right">22.47</td>
    <td align="right">22.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.40</td>
    <td align="right">17.65</td>
    <td align="right">17.69</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.12</td>
    <td align="right">32.25</td>
    <td align="right">32.27</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.94</td>
    <td align="right">30.99</td>
    <td align="right">31.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.02</td>
    <td align="right">21.03</td>
    <td align="right">20.88</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.08</td>
    <td align="right">35.63</td>
    <td align="right">35.58</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.90</td>
    <td align="right">35.72</td>
    <td align="right">35.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">13.32</td>
    <td align="right">16.14</td>
    <td align="right">19.92</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.49</td>
    <td align="right">34.27</td>
    <td align="right">37.42</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">21.39</td>
    <td align="right">24.52</td>
    <td align="right">24.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.76</td>
    <td align="right">23.44</td>
    <td align="right">20.69</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.80</td>
    <td align="right">37.60</td>
    <td align="right">35.97</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">27.94</td>
    <td align="right">32.19</td>
    <td align="right">32.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.02</td>
    <td align="right">30.11</td>
    <td align="right">20.59</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">60.21</td>
    <td align="right">45.70</td>
    <td align="right">38.07</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">30.02</td>
    <td align="right">35.19</td>
    <td align="right">35.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">29.80</td>
    <td align="right">35.46</td>
    <td align="right">21.33</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">66.38</td>
    <td align="right">47.68</td>
    <td align="right">37.49</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">42.26</td>
    <td align="right">46.01</td>
    <td align="right">46.35</td>
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
    <td align="right">107.04</td>
    <td align="right">57.68</td>
    <td align="right">24.69</td>
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
    <td align="right">14.61</td>
    <td align="right">24.10</td>
    <td align="right">28.90</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">11.76</td>
    <td align="right">13.47</td>
    <td align="right">13.78</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">39.01</td>
    <td align="right">15.34</td>
    <td align="right">15.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">24.48</td>
    <td align="right">45.34</td>
    <td align="right">39.35</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">51.04</td>
    <td align="right">38.20</td>
    <td align="right">37.31</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">34.28</td>
    <td align="right">31.49</td>
    <td align="right">39.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">81.77</td>
    <td align="right">118.70</td>
    <td align="right">55.57</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">48.57</td>
    <td align="right">43.34</td>
    <td align="right">42.51</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">47.68</td>
    <td align="right">48.54</td>
    <td align="right">45.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">130.62</td>
    <td align="right">211.48</td>
    <td align="right">74.88</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">48.11</td>
    <td align="right">49.56</td>
    <td align="right">52.74</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">48.54</td>
    <td align="right">57.45</td>
    <td align="right">50.36</td>
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
    <td align="right">15.27</td>
    <td align="right">21.52</td>
    <td align="right">18.96</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">16.07</td>
    <td align="right">25.18</td>
    <td align="right">17.95</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">8.27</td>
    <td align="right">9.77</td>
    <td align="right">9.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">35.48</td>
    <td align="right">42.66</td>
    <td align="right">35.52</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">43.45</td>
    <td align="right">49.23</td>
    <td align="right">39.69</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">18.84</td>
    <td align="right">23.02</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">61.14</td>
    <td align="right">89.77</td>
    <td align="right">81.31</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">85.74</td>
    <td align="right">84.24</td>
    <td align="right">80.24</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">36.13</td>
    <td align="right">45.55</td>
    <td align="right">41.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">80.87</td>
    <td align="right">88.44</td>
    <td align="right">93.78</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">106.33</td>
    <td align="right">95.28</td>
    <td align="right">98.33</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">52.63</td>
    <td align="right">63.67</td>
    <td align="right">60.83</td>
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
    <td align="right">7.37</td>
    <td align="right">12.67</td>
    <td align="right">11.05</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.58</td>
    <td align="right">21.23</td>
    <td align="right">19.72</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">16.80</td>
    <td align="right">23.77</td>
    <td align="right">19.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">13.77</td>
    <td align="right">23.16</td>
    <td align="right">17.82</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">27.60</td>
    <td align="right">36.91</td>
    <td align="right">40.34</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">42.44</td>
    <td align="right">43.23</td>
    <td align="right">34.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">32.43</td>
    <td align="right">48.54</td>
    <td align="right">49.11</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">56.28</td>
    <td align="right">76.18</td>
    <td align="right">75.51</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">83.45</td>
    <td align="right">79.19</td>
    <td align="right">85.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">59.72</td>
    <td align="right">60.77</td>
    <td align="right">61.00</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">82.01</td>
    <td align="right">101.80</td>
    <td align="right">96.32</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">114.53</td>
    <td align="right">99.59</td>
    <td align="right">95.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">17.56</td>
    <td align="right">22.79</td>
    <td align="right">27.62</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">76.83</td>
    <td align="right">54.95</td>
    <td align="right">59.12</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">22.20</td>
    <td align="right">26.16</td>
    <td align="right">26.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">34.09</td>
    <td align="right">66.84</td>
    <td align="right">35.86</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">113.41</td>
    <td align="right">95.12</td>
    <td align="right">60.51</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">29.88</td>
    <td align="right">34.57</td>
    <td align="right">34.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">70.33</td>
    <td align="right">74.84</td>
    <td align="right">37.60</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">124.28</td>
    <td align="right">110.51</td>
    <td align="right">68.16</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">37.40</td>
    <td align="right">38.88</td>
    <td align="right">45.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">92.17</td>
    <td align="right">104.16</td>
    <td align="right">44.95</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">136.39</td>
    <td align="right">124.51</td>
    <td align="right">73.04</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">69.85</td>
    <td align="right">81.13</td>
    <td align="right">71.31</td>
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
    <td align="right">43.45</td>
    <td align="right">8.79</td>
    <td align="right">6.70</td>
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
    <td align="right">59.85</td>
    <td align="right">55.03</td>
    <td align="right">41.53</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.14</td>
    <td align="right">19.64</td>
    <td align="right">23.36</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.66</td>
    <td align="right">21.58</td>
    <td align="right">24.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">90.29</td>
    <td align="right">80.40</td>
    <td align="right">44.05</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.32</td>
    <td align="right">21.28</td>
    <td align="right">23.83</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.25</td>
    <td align="right">22.33</td>
    <td align="right">24.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.68</td>
    <td align="right">100.47</td>
    <td align="right">44.49</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.16</td>
    <td align="right">22.63</td>
    <td align="right">24.44</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">28.08</td>
    <td align="right">24.21</td>
    <td align="right">25.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">141.07</td>
    <td align="right">126.13</td>
    <td align="right">45.26</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.22</td>
    <td align="right">24.34</td>
    <td align="right">25.26</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">29.91</td>
    <td align="right">25.58</td>
    <td align="right">26.30</td>
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
    <td align="right">22.97</td>
    <td align="right">41.22</td>
    <td align="right">41.44</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">29.61</td>
    <td align="right">41.68</td>
    <td align="right">41.32</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.63</td>
    <td align="right">25.52</td>
    <td align="right">25.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">27.83</td>
    <td align="right">56.38</td>
    <td align="right">56.82</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.44</td>
    <td align="right">57.74</td>
    <td align="right">57.94</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.55</td>
    <td align="right">36.37</td>
    <td align="right">25.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.81</td>
    <td align="right">76.88</td>
    <td align="right">76.76</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.86</td>
    <td align="right">77.77</td>
    <td align="right">77.82</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.13</td>
    <td align="right">54.74</td>
    <td align="right">39.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.22</td>
    <td align="right">86.18</td>
    <td align="right">86.18</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">49.82</td>
    <td align="right">92.51</td>
    <td align="right">92.30</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.09</td>
    <td align="right">55.90</td>
    <td align="right">39.96</td>
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
    <td align="right">26.12</td>
    <td align="right">26.29</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.66</td>
    <td align="right">28.88</td>
    <td align="right">28.89</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.89</td>
    <td align="right">30.84</td>
    <td align="right">30.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.88</td>
    <td align="right">46.59</td>
    <td align="right">35.45</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.61</td>
    <td align="right">39.63</td>
    <td align="right">27.52</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.16</td>
    <td align="right">51.75</td>
    <td align="right">40.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.74</td>
    <td align="right">55.08</td>
    <td align="right">39.05</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.14</td>
    <td align="right">53.08</td>
    <td align="right">34.92</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.20</td>
    <td align="right">61.60</td>
    <td align="right">43.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.85</td>
    <td align="right">55.04</td>
    <td align="right">39.59</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.64</td>
    <td align="right">64.97</td>
    <td align="right">44.40</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.42</td>
    <td align="right">64.23</td>
    <td align="right">44.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">25.15</td>
    <td align="right">42.81</td>
    <td align="right">35.10</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.56</td>
    <td align="right">53.69</td>
    <td align="right">40.10</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">36.72</td>
    <td align="right">59.96</td>
    <td align="right">60.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">36.09</td>
    <td align="right">60.32</td>
    <td align="right">35.51</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">40.97</td>
    <td align="right">61.41</td>
    <td align="right">38.10</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">45.46</td>
    <td align="right">77.38</td>
    <td align="right">77.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">40.73</td>
    <td align="right">73.85</td>
    <td align="right">36.12</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.58</td>
    <td align="right">79.58</td>
    <td align="right">39.96</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">48.85</td>
    <td align="right">83.72</td>
    <td align="right">83.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">52.85</td>
    <td align="right">93.65</td>
    <td align="right">37.43</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">58.15</td>
    <td align="right">94.47</td>
    <td align="right">39.28</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">66.93</td>
    <td align="right">118.60</td>
    <td align="right">118.81</td>
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
    <td align="right">68.67</td>
    <td align="right">37.20</td>
    <td align="right">16.72</td>
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
    <td align="right">69.91</td>
    <td align="right">62.18</td>
    <td align="right">47.70</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">25.58</td>
    <td align="right">22.15</td>
    <td align="right">30.46</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">28.99</td>
    <td align="right">24.63</td>
    <td align="right">29.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">144.32</td>
    <td align="right">112.56</td>
    <td align="right">55.43</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">47.17</td>
    <td align="right">32.20</td>
    <td align="right">38.14</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">45.53</td>
    <td align="right">41.25</td>
    <td align="right">38.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">217.10</td>
    <td align="right">162.66</td>
    <td align="right">50.82</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">34.12</td>
    <td align="right">34.61</td>
    <td align="right">36.04</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">67.90</td>
    <td align="right">30.15</td>
    <td align="right">32.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">244.63</td>
    <td align="right">214.54</td>
    <td align="right">60.24</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">38.83</td>
    <td align="right">33.77</td>
    <td align="right">37.54</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">39.82</td>
    <td align="right">29.78</td>
    <td align="right">43.87</td>
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
    <td align="right">25.65</td>
    <td align="right">42.21</td>
    <td align="right">42.67</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.62</td>
    <td align="right">43.66</td>
    <td align="right">42.71</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.22</td>
    <td align="right">30.34</td>
    <td align="right">30.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">31.09</td>
    <td align="right">68.76</td>
    <td align="right">60.51</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">36.75</td>
    <td align="right">68.37</td>
    <td align="right">67.34</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">20.31</td>
    <td align="right">42.15</td>
    <td align="right">43.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">44.87</td>
    <td align="right">82.32</td>
    <td align="right">81.97</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">59.37</td>
    <td align="right">88.30</td>
    <td align="right">87.14</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">41.67</td>
    <td align="right">69.63</td>
    <td align="right">58.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">53.49</td>
    <td align="right">97.32</td>
    <td align="right">94.90</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">61.07</td>
    <td align="right">108.42</td>
    <td align="right">112.12</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">57.85</td>
    <td align="right">98.62</td>
    <td align="right">76.50</td>
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
    <td align="right">20.22</td>
    <td align="right">31.63</td>
    <td align="right">31.24</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">22.57</td>
    <td align="right">33.55</td>
    <td align="right">33.50</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">21.93</td>
    <td align="right">37.66</td>
    <td align="right">35.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.14</td>
    <td align="right">52.59</td>
    <td align="right">51.53</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">20.22</td>
    <td align="right">48.60</td>
    <td align="right">32.26</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">24.24</td>
    <td align="right">62.47</td>
    <td align="right">46.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">44.61</td>
    <td align="right">89.32</td>
    <td align="right">62.71</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">36.34</td>
    <td align="right">60.04</td>
    <td align="right">44.09</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">34.31</td>
    <td align="right">67.70</td>
    <td align="right">48.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">43.53</td>
    <td align="right">84.57</td>
    <td align="right">59.01</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">39.15</td>
    <td align="right">97.13</td>
    <td align="right">64.16</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">49.43</td>
    <td align="right">79.00</td>
    <td align="right">56.82</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">27.67</td>
    <td align="right">44.36</td>
    <td align="right">39.05</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">44.92</td>
    <td align="right">56.49</td>
    <td align="right">44.73</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">40.70</td>
    <td align="right">61.20</td>
    <td align="right">61.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">54.46</td>
    <td align="right">69.40</td>
    <td align="right">40.27</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">58.13</td>
    <td align="right">80.34</td>
    <td align="right">49.08</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">49.07</td>
    <td align="right">78.84</td>
    <td align="right">78.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">48.11</td>
    <td align="right">88.35</td>
    <td align="right">44.49</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">74.56</td>
    <td align="right">106.83</td>
    <td align="right">48.96</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">52.32</td>
    <td align="right">89.93</td>
    <td align="right">89.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">78.67</td>
    <td align="right">115.75</td>
    <td align="right">59.86</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">113.85</td>
    <td align="right">155.55</td>
    <td align="right">76.18</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">96.02</td>
    <td align="right">140.83</td>
    <td align="right">132.68</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
