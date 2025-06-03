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
    <td align="right">27.49</td>
    <td align="right">4.45</td>
    <td align="right">3.65</td>
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
    <td align="right">11.12</td>
    <td align="right">10.86</td>
    <td align="right">16.56</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.00</td>
    <td align="right">4.37</td>
    <td align="right">4.38</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.88</td>
    <td align="right">5.07</td>
    <td align="right">5.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.85</td>
    <td align="right">15.82</td>
    <td align="right">17.71</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.82</td>
    <td align="right">4.95</td>
    <td align="right">4.99</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.43</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.71</td>
    <td align="right">18.79</td>
    <td align="right">16.63</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.47</td>
    <td align="right">5.32</td>
    <td align="right">5.38</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.28</td>
    <td align="right">6.32</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.51</td>
    <td align="right">23.48</td>
    <td align="right">17.05</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.19</td>
    <td align="right">5.97</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.88</td>
    <td align="right">6.59</td>
    <td align="right">6.77</td>
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
    <td align="right">5.07</td>
    <td align="right">5.81</td>
    <td align="right">5.78</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">4.99</td>
    <td align="right">5.79</td>
    <td align="right">5.71</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.96</td>
    <td align="right">3.30</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.52</td>
    <td align="right">8.90</td>
    <td align="right">9.00</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.26</td>
    <td align="right">10.02</td>
    <td align="right">9.80</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.47</td>
    <td align="right">3.11</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.51</td>
    <td align="right">13.69</td>
    <td align="right">14.03</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.71</td>
    <td align="right">14.13</td>
    <td align="right">14.02</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.70</td>
    <td align="right">5.77</td>
    <td align="right">3.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.99</td>
    <td align="right">15.36</td>
    <td align="right">15.40</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.17</td>
    <td align="right">17.37</td>
    <td align="right">17.34</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.74</td>
    <td align="right">5.82</td>
    <td align="right">3.89</td>
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
    <td align="right">3.25</td>
    <td align="right">3.23</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.37</td>
    <td align="right">5.07</td>
    <td align="right">5.01</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.58</td>
    <td align="right">4.98</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.08</td>
    <td align="right">3.41</td>
    <td align="right">3.32</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.22</td>
    <td align="right">4.48</td>
    <td align="right">4.49</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.45</td>
    <td align="right">5.12</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.49</td>
    <td align="right">5.64</td>
    <td align="right">3.87</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.11</td>
    <td align="right">7.80</td>
    <td align="right">5.88</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.00</td>
    <td align="right">7.65</td>
    <td align="right">5.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.48</td>
    <td align="right">5.53</td>
    <td align="right">3.91</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.04</td>
    <td align="right">9.13</td>
    <td align="right">6.14</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.40</td>
    <td align="right">9.11</td>
    <td align="right">5.98</td>
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
    <td align="right">31.29</td>
    <td align="right">19.00</td>
    <td align="right">7.37</td>
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
    <td align="right">13.32</td>
    <td align="right">12.68</td>
    <td align="right">17.40</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.62</td>
    <td align="right">4.94</td>
    <td align="right">5.12</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.60</td>
    <td align="right">5.85</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.83</td>
    <td align="right">18.33</td>
    <td align="right">18.09</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.37</td>
    <td align="right">5.44</td>
    <td align="right">5.77</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.05</td>
    <td align="right">6.16</td>
    <td align="right">5.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">25.63</td>
    <td align="right">24.49</td>
    <td align="right">17.80</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.24</td>
    <td align="right">8.81</td>
    <td align="right">11.24</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.69</td>
    <td align="right">8.34</td>
    <td align="right">7.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">42.59</td>
    <td align="right">38.63</td>
    <td align="right">18.65</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">7.85</td>
    <td align="right">7.62</td>
    <td align="right">7.75</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.17</td>
    <td align="right">7.96</td>
    <td align="right">7.95</td>
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
    <td align="right">5.80</td>
    <td align="right">6.61</td>
    <td align="right">6.62</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.99</td>
    <td align="right">7.58</td>
    <td align="right">7.52</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.43</td>
    <td align="right">3.87</td>
    <td align="right">3.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.85</td>
    <td align="right">9.28</td>
    <td align="right">9.28</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.73</td>
    <td align="right">18.66</td>
    <td align="right">16.05</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.21</td>
    <td align="right">4.20</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.87</td>
    <td align="right">15.00</td>
    <td align="right">15.45</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.80</td>
    <td align="right">15.76</td>
    <td align="right">16.14</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.71</td>
    <td align="right">7.01</td>
    <td align="right">7.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.47</td>
    <td align="right">18.28</td>
    <td align="right">18.83</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.39</td>
    <td align="right">21.44</td>
    <td align="right">21.43</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.08</td>
    <td align="right">10.36</td>
    <td align="right">11.24</td>
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
    <td align="right">3.44</td>
    <td align="right">3.90</td>
    <td align="right">3.90</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.12</td>
    <td align="right">5.91</td>
    <td align="right">5.79</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.20</td>
    <td align="right">5.73</td>
    <td align="right">5.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.40</td>
    <td align="right">3.77</td>
    <td align="right">3.82</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.54</td>
    <td align="right">4.89</td>
    <td align="right">4.84</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.59</td>
    <td align="right">5.65</td>
    <td align="right">5.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.01</td>
    <td align="right">7.15</td>
    <td align="right">4.92</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.24</td>
    <td align="right">9.33</td>
    <td align="right">7.21</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.54</td>
    <td align="right">9.64</td>
    <td align="right">8.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.24</td>
    <td align="right">9.39</td>
    <td align="right">7.03</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">11.82</td>
    <td align="right">13.82</td>
    <td align="right">8.47</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.52</td>
    <td align="right">13.95</td>
    <td align="right">9.51</td>
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
    <td align="right">26.39</td>
    <td align="right">4.17</td>
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
    <td align="right">9.53</td>
    <td align="right">9.18</td>
    <td align="right">15.62</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.32</td>
    <td align="right">4.07</td>
    <td align="right">3.97</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.88</td>
    <td align="right">4.57</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.88</td>
    <td align="right">13.68</td>
    <td align="right">16.58</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.84</td>
    <td align="right">4.73</td>
    <td align="right">4.57</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.48</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.28</td>
    <td align="right">16.61</td>
    <td align="right">15.87</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.35</td>
    <td align="right">5.26</td>
    <td align="right">5.09</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.95</td>
    <td align="right">6.01</td>
    <td align="right">6.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.35</td>
    <td align="right">22.96</td>
    <td align="right">15.90</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.82</td>
    <td align="right">5.69</td>
    <td align="right">5.74</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.96</td>
    <td align="right">3.28</td>
    <td align="right">3.29</td>
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
    <td align="right">3.07</td>
    <td align="right">3.61</td>
    <td align="right">3.59</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.15</td>
    <td align="right">3.51</td>
    <td align="right">3.52</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.58</td>
    <td align="right">2.50</td>
    <td align="right">2.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.70</td>
    <td align="right">4.08</td>
    <td align="right">4.12</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.74</td>
    <td align="right">4.43</td>
    <td align="right">4.42</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.14</td>
    <td align="right">2.26</td>
    <td align="right">2.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.61</td>
    <td align="right">7.15</td>
    <td align="right">7.14</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.77</td>
    <td align="right">6.99</td>
    <td align="right">7.04</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.18</td>
    <td align="right">4.36</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.00</td>
    <td align="right">7.60</td>
    <td align="right">7.64</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.33</td>
    <td align="right">8.14</td>
    <td align="right">8.14</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.22</td>
    <td align="right">4.39</td>
    <td align="right">3.15</td>
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
    <td align="right">2.61</td>
    <td align="right">2.33</td>
    <td align="right">2.33</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.64</td>
    <td align="right">4.06</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.69</td>
    <td align="right">3.91</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.69</td>
    <td align="right">2.42</td>
    <td align="right">2.43</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.94</td>
    <td align="right">3.72</td>
    <td align="right">3.73</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.85</td>
    <td align="right">4.02</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.22</td>
    <td align="right">4.31</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.68</td>
    <td align="right">6.03</td>
    <td align="right">4.65</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.83</td>
    <td align="right">6.02</td>
    <td align="right">4.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.29</td>
    <td align="right">4.35</td>
    <td align="right">2.94</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.67</td>
    <td align="right">7.19</td>
    <td align="right">4.69</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.86</td>
    <td align="right">7.09</td>
    <td align="right">4.59</td>
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
    <td align="right">31.48</td>
    <td align="right">16.25</td>
    <td align="right">6.35</td>
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
    <td align="right">11.25</td>
    <td align="right">10.97</td>
    <td align="right">16.83</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.03</td>
    <td align="right">4.79</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.73</td>
    <td align="right">5.46</td>
    <td align="right">5.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.07</td>
    <td align="right">15.95</td>
    <td align="right">17.47</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.52</td>
    <td align="right">5.30</td>
    <td align="right">5.14</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.24</td>
    <td align="right">6.04</td>
    <td align="right">6.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">20.01</td>
    <td align="right">20.46</td>
    <td align="right">16.85</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.34</td>
    <td align="right">6.16</td>
    <td align="right">6.02</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.03</td>
    <td align="right">6.99</td>
    <td align="right">7.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">32.02</td>
    <td align="right">32.51</td>
    <td align="right">17.30</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">7.58</td>
    <td align="right">8.06</td>
    <td align="right">8.01</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.38</td>
    <td align="right">4.86</td>
    <td align="right">4.84</td>
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
    <td align="right">3.72</td>
    <td align="right">4.37</td>
    <td align="right">4.35</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.81</td>
    <td align="right">4.24</td>
    <td align="right">4.26</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.16</td>
    <td align="right">3.15</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.20</td>
    <td align="right">4.70</td>
    <td align="right">4.72</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.24</td>
    <td align="right">5.15</td>
    <td align="right">5.15</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.54</td>
    <td align="right">2.69</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.88</td>
    <td align="right">7.03</td>
    <td align="right">6.99</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.11</td>
    <td align="right">8.79</td>
    <td align="right">8.86</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">4.99</td>
    <td align="right">5.35</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.26</td>
    <td align="right">10.48</td>
    <td align="right">10.30</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">8.17</td>
    <td align="right">10.65</td>
    <td align="right">11.12</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">6.36</td>
    <td align="right">7.09</td>
    <td align="right">5.03</td>
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
    <td align="right">3.14</td>
    <td align="right">2.98</td>
    <td align="right">2.97</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.37</td>
    <td align="right">4.89</td>
    <td align="right">4.90</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.39</td>
    <td align="right">4.77</td>
    <td align="right">4.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.11</td>
    <td align="right">3.02</td>
    <td align="right">2.98</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.46</td>
    <td align="right">4.31</td>
    <td align="right">4.30</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.47</td>
    <td align="right">4.88</td>
    <td align="right">4.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.18</td>
    <td align="right">5.51</td>
    <td align="right">3.88</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">7.10</td>
    <td align="right">7.61</td>
    <td align="right">6.04</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.10</td>
    <td align="right">8.25</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">6.97</td>
    <td align="right">7.38</td>
    <td align="right">5.00</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">8.72</td>
    <td align="right">9.62</td>
    <td align="right">6.46</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">9.08</td>
    <td align="right">9.97</td>
    <td align="right">6.75</td>
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
    <td align="right">21.38</td>
    <td align="right">4.25</td>
    <td align="right">3.23</td>
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
    <td align="right">6.65</td>
    <td align="right">4.75</td>
    <td align="right">13.74</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.40</td>
    <td align="right">1.28</td>
    <td align="right">1.38</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.72</td>
    <td align="right">1.36</td>
    <td align="right">1.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.82</td>
    <td align="right">7.60</td>
    <td align="right">13.24</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.50</td>
    <td align="right">1.68</td>
    <td align="right">1.56</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.89</td>
    <td align="right">1.59</td>
    <td align="right">1.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">12.40</td>
    <td align="right">10.18</td>
    <td align="right">14.46</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="right">1.90</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.06</td>
    <td align="right">1.76</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">18.81</td>
    <td align="right">10.70</td>
    <td align="right">11.23</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.01</td>
    <td align="right">2.09</td>
    <td align="right">2.13</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.94</td>
    <td align="right">1.79</td>
    <td align="right">1.69</td>
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
    <td align="right">2.55</td>
    <td align="right">1.83</td>
    <td align="right">1.81</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.59</td>
    <td align="right">1.88</td>
    <td align="right">1.83</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.20</td>
    <td align="right">1.91</td>
    <td align="right">1.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.44</td>
    <td align="right">2.22</td>
    <td align="right">2.04</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.11</td>
    <td align="right">2.58</td>
    <td align="right">2.63</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.88</td>
    <td align="right">1.61</td>
    <td align="right">1.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.17</td>
    <td align="right">3.12</td>
    <td align="right">3.29</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.69</td>
    <td align="right">3.47</td>
    <td align="right">3.31</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">2.94</td>
    <td align="right">2.40</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.18</td>
    <td align="right">3.76</td>
    <td align="right">3.98</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.44</td>
    <td align="right">4.36</td>
    <td align="right">4.47</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.31</td>
    <td align="right">3.61</td>
    <td align="right">1.89</td>
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
    <td align="right">2.22</td>
    <td align="right">2.18</td>
    <td align="right">1.82</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.50</td>
    <td align="right">1.87</td>
    <td align="right">1.84</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.47</td>
    <td align="right">1.91</td>
    <td align="right">1.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.22</td>
    <td align="right">1.76</td>
    <td align="right">1.74</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.42</td>
    <td align="right">2.13</td>
    <td align="right">2.20</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.03</td>
    <td align="right">2.33</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">8.30</td>
    <td align="right">7.24</td>
    <td align="right">1.87</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.56</td>
    <td align="right">3.21</td>
    <td align="right">3.27</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.62</td>
    <td align="right">3.35</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.38</td>
    <td align="right">3.88</td>
    <td align="right">2.03</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.28</td>
    <td align="right">4.09</td>
    <td align="right">4.45</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.60</td>
    <td align="right">4.47</td>
    <td align="right">4.48</td>
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
    <td align="right">36.21</td>
    <td align="right">18.26</td>
    <td align="right">13.46</td>
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
    <td align="right">19.36</td>
    <td align="right">24.71</td>
    <td align="right">32.14</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.33</td>
    <td align="right">9.66</td>
    <td align="right">9.08</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.84</td>
    <td align="right">8.35</td>
    <td align="right">8.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">58.22</td>
    <td align="right">41.98</td>
    <td align="right">30.73</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.49</td>
    <td align="right">9.12</td>
    <td align="right">10.25</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.06</td>
    <td align="right">8.36</td>
    <td align="right">11.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">49.61</td>
    <td align="right">42.09</td>
    <td align="right">22.90</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.09</td>
    <td align="right">8.18</td>
    <td align="right">8.30</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.86</td>
    <td align="right">10.77</td>
    <td align="right">10.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">80.73</td>
    <td align="right">61.63</td>
    <td align="right">27.66</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.97</td>
    <td align="right">11.82</td>
    <td align="right">14.59</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.09</td>
    <td align="right">10.34</td>
    <td align="right">10.63</td>
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
    <td align="right">4.49</td>
    <td align="right">5.45</td>
    <td align="right">5.66</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.79</td>
    <td align="right">5.98</td>
    <td align="right">4.91</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.86</td>
    <td align="right">8.82</td>
    <td align="right">7.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.52</td>
    <td align="right">9.31</td>
    <td align="right">9.02</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.70</td>
    <td align="right">10.99</td>
    <td align="right">9.53</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.17</td>
    <td align="right">7.08</td>
    <td align="right">7.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.14</td>
    <td align="right">18.99</td>
    <td align="right">18.33</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.50</td>
    <td align="right">19.31</td>
    <td align="right">18.78</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">12.01</td>
    <td align="right">13.41</td>
    <td align="right">9.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">23.42</td>
    <td align="right">19.72</td>
    <td align="right">21.84</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">25.45</td>
    <td align="right">22.44</td>
    <td align="right">23.78</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">11.84</td>
    <td align="right">12.08</td>
    <td align="right">6.64</td>
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
    <td align="right">2.49</td>
    <td align="right">3.54</td>
    <td align="right">3.03</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.85</td>
    <td align="right">2.73</td>
    <td align="right">2.74</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.98</td>
    <td align="right">2.74</td>
    <td align="right">2.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">4.25</td>
    <td align="right">4.86</td>
    <td align="right">3.31</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.61</td>
    <td align="right">6.50</td>
    <td align="right">6.74</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">6.19</td>
    <td align="right">5.34</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">9.99</td>
    <td align="right">10.05</td>
    <td align="right">6.97</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.69</td>
    <td align="right">11.06</td>
    <td align="right">12.48</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.78</td>
    <td align="right">9.45</td>
    <td align="right">9.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.49</td>
    <td align="right">12.75</td>
    <td align="right">7.15</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.79</td>
    <td align="right">18.63</td>
    <td align="right">18.50</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.77</td>
    <td align="right">22.47</td>
    <td align="right">22.32</td>
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
    <td align="right">34.74</td>
    <td align="right">5.60</td>
    <td align="right">3.58</td>
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
    <td align="right">12.15</td>
    <td align="right">12.58</td>
    <td align="right">17.46</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.84</td>
    <td align="right">4.26</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.94</td>
    <td align="right">5.19</td>
    <td align="right">5.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.56</td>
    <td align="right">17.76</td>
    <td align="right">17.57</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.96</td>
    <td align="right">4.77</td>
    <td align="right">4.78</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.03</td>
    <td align="right">5.86</td>
    <td align="right">6.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.83</td>
    <td align="right">21.41</td>
    <td align="right">17.19</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.61</td>
    <td align="right">5.31</td>
    <td align="right">5.32</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.32</td>
    <td align="right">6.94</td>
    <td align="right">6.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.26</td>
    <td align="right">26.75</td>
    <td align="right">17.13</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">10.04</td>
    <td align="right">5.95</td>
    <td align="right">5.90</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.38</td>
    <td align="right">7.39</td>
    <td align="right">7.54</td>
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
    <td align="right">7.84</td>
    <td align="right">5.51</td>
    <td align="right">5.50</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">10.44</td>
    <td align="right">5.59</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.33</td>
    <td align="right">3.91</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.45</td>
    <td align="right">8.21</td>
    <td align="right">8.15</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.40</td>
    <td align="right">8.76</td>
    <td align="right">7.88</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.92</td>
    <td align="right">4.86</td>
    <td align="right">4.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">16.74</td>
    <td align="right">10.98</td>
    <td align="right">10.96</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.07</td>
    <td align="right">10.43</td>
    <td align="right">10.56</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.04</td>
    <td align="right">6.99</td>
    <td align="right">5.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.64</td>
    <td align="right">13.93</td>
    <td align="right">13.92</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.95</td>
    <td align="right">13.73</td>
    <td align="right">13.72</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.15</td>
    <td align="right">7.13</td>
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
    <td align="right">3.28</td>
    <td align="right">3.91</td>
    <td align="right">3.90</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.48</td>
    <td align="right">5.51</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.65</td>
    <td align="right">5.47</td>
    <td align="right">5.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.34</td>
    <td align="right">5.53</td>
    <td align="right">4.64</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.88</td>
    <td align="right">5.82</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.95</td>
    <td align="right">7.05</td>
    <td align="right">6.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.05</td>
    <td align="right">6.93</td>
    <td align="right">5.02</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.83</td>
    <td align="right">9.28</td>
    <td align="right">7.48</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.61</td>
    <td align="right">9.35</td>
    <td align="right">7.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.14</td>
    <td align="right">6.89</td>
    <td align="right">5.12</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.15</td>
    <td align="right">10.62</td>
    <td align="right">7.65</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.25</td>
    <td align="right">10.33</td>
    <td align="right">7.42</td>
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
    <td align="right">45.08</td>
    <td align="right">21.42</td>
    <td align="right">8.79</td>
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
    <td align="right">14.60</td>
    <td align="right">13.06</td>
    <td align="right">18.15</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.25</td>
    <td align="right">4.72</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.98</td>
    <td align="right">5.91</td>
    <td align="right">5.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">23.31</td>
    <td align="right">19.82</td>
    <td align="right">18.62</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.46</td>
    <td align="right">5.55</td>
    <td align="right">5.32</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.90</td>
    <td align="right">6.72</td>
    <td align="right">6.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">38.61</td>
    <td align="right">37.13</td>
    <td align="right">19.57</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">13.01</td>
    <td align="right">8.97</td>
    <td align="right">11.47</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">15.49</td>
    <td align="right">12.92</td>
    <td align="right">12.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">79.01</td>
    <td align="right">80.32</td>
    <td align="right">23.71</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">18.46</td>
    <td align="right">13.85</td>
    <td align="right">14.91</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">17.14</td>
    <td align="right">12.97</td>
    <td align="right">12.56</td>
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
    <td align="right">9.34</td>
    <td align="right">6.22</td>
    <td align="right">6.16</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">10.72</td>
    <td align="right">6.39</td>
    <td align="right">6.32</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.68</td>
    <td align="right">4.21</td>
    <td align="right">4.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.71</td>
    <td align="right">9.55</td>
    <td align="right">9.64</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.59</td>
    <td align="right">9.25</td>
    <td align="right">8.57</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.20</td>
    <td align="right">5.26</td>
    <td align="right">4.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">23.33</td>
    <td align="right">15.12</td>
    <td align="right">14.78</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.56</td>
    <td align="right">15.92</td>
    <td align="right">13.17</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.77</td>
    <td align="right">7.74</td>
    <td align="right">5.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">23.21</td>
    <td align="right">20.06</td>
    <td align="right">22.62</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.59</td>
    <td align="right">17.66</td>
    <td align="right">17.69</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">8.64</td>
    <td align="right">10.70</td>
    <td align="right">8.61</td>
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
    <td align="right">3.62</td>
    <td align="right">4.12</td>
    <td align="right">4.16</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.95</td>
    <td align="right">5.87</td>
    <td align="right">5.88</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.10</td>
    <td align="right">5.84</td>
    <td align="right">5.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.83</td>
    <td align="right">6.26</td>
    <td align="right">5.15</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.47</td>
    <td align="right">6.37</td>
    <td align="right">5.98</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.49</td>
    <td align="right">7.58</td>
    <td align="right">6.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.92</td>
    <td align="right">7.63</td>
    <td align="right">5.53</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.78</td>
    <td align="right">10.19</td>
    <td align="right">8.36</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.60</td>
    <td align="right">11.20</td>
    <td align="right">10.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">15.48</td>
    <td align="right">20.88</td>
    <td align="right">15.11</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">14.28</td>
    <td align="right">20.97</td>
    <td align="right">12.30</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.07</td>
    <td align="right">13.78</td>
    <td align="right">9.93</td>
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
    <td align="right">64.22</td>
    <td align="right">37.91</td>
    <td align="right">16.38</td>
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
    <td align="right">28.02</td>
    <td align="right">43.06</td>
    <td align="right">36.88</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.61</td>
    <td align="right">15.82</td>
    <td align="right">15.65</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.44</td>
    <td align="right">19.35</td>
    <td align="right">19.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">38.16</td>
    <td align="right">65.55</td>
    <td align="right">41.30</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.40</td>
    <td align="right">19.57</td>
    <td align="right">19.78</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.23</td>
    <td align="right">18.70</td>
    <td align="right">18.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.64</td>
    <td align="right">78.81</td>
    <td align="right">38.22</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.42</td>
    <td align="right">18.64</td>
    <td align="right">18.47</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.22</td>
    <td align="right">18.67</td>
    <td align="right">18.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">57.99</td>
    <td align="right">98.47</td>
    <td align="right">38.14</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.24</td>
    <td align="right">18.75</td>
    <td align="right">18.83</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.14</td>
    <td align="right">19.92</td>
    <td align="right">20.13</td>
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
    <td align="right">16.28</td>
    <td align="right">21.65</td>
    <td align="right">21.26</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.98</td>
    <td align="right">22.45</td>
    <td align="right">22.35</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">11.15</td>
    <td align="right">13.83</td>
    <td align="right">13.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.59</td>
    <td align="right">26.24</td>
    <td align="right">26.23</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.84</td>
    <td align="right">27.99</td>
    <td align="right">27.85</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.95</td>
    <td align="right">15.82</td>
    <td align="right">15.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.49</td>
    <td align="right">33.43</td>
    <td align="right">33.35</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.20</td>
    <td align="right">47.03</td>
    <td align="right">46.85</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">15.29</td>
    <td align="right">19.57</td>
    <td align="right">19.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.42</td>
    <td align="right">36.46</td>
    <td align="right">36.13</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">78.20</td>
    <td align="right">56.79</td>
    <td align="right">56.69</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.41</td>
    <td align="right">25.64</td>
    <td align="right">25.56</td>
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
    <td align="right">15.54</td>
    <td align="right">15.67</td>
    <td align="right">15.67</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.36</td>
    <td align="right">21.24</td>
    <td align="right">21.21</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.78</td>
    <td align="right">22.18</td>
    <td align="right">22.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">20.14</td>
    <td align="right">20.53</td>
    <td align="right">20.57</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.52</td>
    <td align="right">26.08</td>
    <td align="right">26.11</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.96</td>
    <td align="right">27.89</td>
    <td align="right">27.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.68</td>
    <td align="right">24.95</td>
    <td align="right">24.85</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.87</td>
    <td align="right">33.30</td>
    <td align="right">33.15</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.41</td>
    <td align="right">46.83</td>
    <td align="right">46.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.64</td>
    <td align="right">37.49</td>
    <td align="right">37.58</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.67</td>
    <td align="right">36.37</td>
    <td align="right">36.81</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">78.23</td>
    <td align="right">56.67</td>
    <td align="right">56.63</td>
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
    <td align="right">76.76</td>
    <td align="right">108.19</td>
    <td align="right">22.26</td>
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
    <td align="right">27.87</td>
    <td align="right">43.52</td>
    <td align="right">39.76</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.10</td>
    <td align="right">16.44</td>
    <td align="right">15.96</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.70</td>
    <td align="right">19.31</td>
    <td align="right">19.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">38.21</td>
    <td align="right">71.24</td>
    <td align="right">54.10</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">22.68</td>
    <td align="right">22.61</td>
    <td align="right">21.91</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">17.39</td>
    <td align="right">19.69</td>
    <td align="right">19.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">49.64</td>
    <td align="right">93.40</td>
    <td align="right">54.87</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">19.57</td>
    <td align="right">25.87</td>
    <td align="right">26.21</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">37.17</td>
    <td align="right">23.65</td>
    <td align="right">47.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">100.76</td>
    <td align="right">183.55</td>
    <td align="right">54.68</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">27.80</td>
    <td align="right">27.78</td>
    <td align="right">30.76</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">34.32</td>
    <td align="right">37.83</td>
    <td align="right">39.98</td>
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
    <td align="right">17.40</td>
    <td align="right">23.30</td>
    <td align="right">23.66</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">35.85</td>
    <td align="right">38.09</td>
    <td align="right">41.19</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">12.01</td>
    <td align="right">14.23</td>
    <td align="right">14.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">25.31</td>
    <td align="right">30.30</td>
    <td align="right">33.89</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">52.41</td>
    <td align="right">43.55</td>
    <td align="right">31.99</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">14.08</td>
    <td align="right">16.56</td>
    <td align="right">16.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.95</td>
    <td align="right">40.71</td>
    <td align="right">46.05</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">70.12</td>
    <td align="right">52.58</td>
    <td align="right">53.26</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">17.39</td>
    <td align="right">25.11</td>
    <td align="right">25.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">49.31</td>
    <td align="right">69.16</td>
    <td align="right">59.67</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">97.74</td>
    <td align="right">73.41</td>
    <td align="right">67.76</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">42.69</td>
    <td align="right">41.77</td>
    <td align="right">37.36</td>
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
    <td align="right">16.07</td>
    <td align="right">16.14</td>
    <td align="right">16.51</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.19</td>
    <td align="right">22.41</td>
    <td align="right">27.67</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">36.37</td>
    <td align="right">25.55</td>
    <td align="right">23.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">24.19</td>
    <td align="right">26.94</td>
    <td align="right">41.60</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">26.66</td>
    <td align="right">26.74</td>
    <td align="right">26.96</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">45.84</td>
    <td align="right">31.43</td>
    <td align="right">33.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">44.35</td>
    <td align="right">51.14</td>
    <td align="right">38.79</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">33.23</td>
    <td align="right">39.98</td>
    <td align="right">40.29</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">69.40</td>
    <td align="right">50.53</td>
    <td align="right">51.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">59.83</td>
    <td align="right">60.96</td>
    <td align="right">64.51</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">42.91</td>
    <td align="right">60.31</td>
    <td align="right">49.77</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">88.07</td>
    <td align="right">66.82</td>
    <td align="right">66.64</td>
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
    <td align="right">63.98</td>
    <td align="right">10.11</td>
    <td align="right">8.12</td>
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
    <td align="right">13.75</td>
    <td align="right">22.77</td>
    <td align="right">26.41</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.49</td>
    <td align="right">12.42</td>
    <td align="right">12.57</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.71</td>
    <td align="right">13.80</td>
    <td align="right">13.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">20.15</td>
    <td align="right">35.16</td>
    <td align="right">28.71</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.09</td>
    <td align="right">14.06</td>
    <td align="right">14.04</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.52</td>
    <td align="right">15.31</td>
    <td align="right">15.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.19</td>
    <td align="right">47.36</td>
    <td align="right">30.16</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.81</td>
    <td align="right">15.37</td>
    <td align="right">15.33</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.57</td>
    <td align="right">16.70</td>
    <td align="right">16.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.75</td>
    <td align="right">60.37</td>
    <td align="right">30.90</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.53</td>
    <td align="right">16.23</td>
    <td align="right">16.24</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.97</td>
    <td align="right">17.94</td>
    <td align="right">17.94</td>
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
    <td align="right">12.67</td>
    <td align="right">16.11</td>
    <td align="right">16.11</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.39</td>
    <td align="right">16.76</td>
    <td align="right">16.76</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.14</td>
    <td align="right">9.39</td>
    <td align="right">9.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.42</td>
    <td align="right">22.48</td>
    <td align="right">22.49</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.32</td>
    <td align="right">22.32</td>
    <td align="right">22.32</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.24</td>
    <td align="right">14.07</td>
    <td align="right">14.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.92</td>
    <td align="right">32.45</td>
    <td align="right">32.28</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.64</td>
    <td align="right">30.77</td>
    <td align="right">30.78</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.98</td>
    <td align="right">17.53</td>
    <td align="right">17.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.29</td>
    <td align="right">36.16</td>
    <td align="right">36.09</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.05</td>
    <td align="right">36.06</td>
    <td align="right">35.97</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.30</td>
    <td align="right">20.49</td>
    <td align="right">20.39</td>
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
    <td align="right">6.57</td>
    <td align="right">9.37</td>
    <td align="right">9.37</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.78</td>
    <td align="right">16.32</td>
    <td align="right">16.13</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.28</td>
    <td align="right">16.75</td>
    <td align="right">16.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.97</td>
    <td align="right">13.70</td>
    <td align="right">13.71</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.43</td>
    <td align="right">22.45</td>
    <td align="right">22.46</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.31</td>
    <td align="right">22.32</td>
    <td align="right">22.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.90</td>
    <td align="right">17.58</td>
    <td align="right">17.62</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.52</td>
    <td align="right">32.48</td>
    <td align="right">32.33</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.76</td>
    <td align="right">30.76</td>
    <td align="right">31.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.09</td>
    <td align="right">21.05</td>
    <td align="right">20.89</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.11</td>
    <td align="right">36.13</td>
    <td align="right">36.09</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.97</td>
    <td align="right">35.91</td>
    <td align="right">36.00</td>
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
    <td align="right">89.69</td>
    <td align="right">50.94</td>
    <td align="right">12.24</td>
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
    <td align="right">14.27</td>
    <td align="right">23.24</td>
    <td align="right">28.50</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.89</td>
    <td align="right">14.49</td>
    <td align="right">16.48</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.91</td>
    <td align="right">14.36</td>
    <td align="right">14.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.58</td>
    <td align="right">36.00</td>
    <td align="right">29.68</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.70</td>
    <td align="right">15.05</td>
    <td align="right">14.65</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">15.56</td>
    <td align="right">45.66</td>
    <td align="right">15.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">30.80</td>
    <td align="right">66.14</td>
    <td align="right">44.81</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">15.45</td>
    <td align="right">16.86</td>
    <td align="right">19.89</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">15.71</td>
    <td align="right">18.09</td>
    <td align="right">22.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">80.43</td>
    <td align="right">116.88</td>
    <td align="right">39.88</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">22.48</td>
    <td align="right">33.61</td>
    <td align="right">22.62</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">23.51</td>
    <td align="right">26.84</td>
    <td align="right">28.52</td>
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
    <td align="right">12.68</td>
    <td align="right">16.67</td>
    <td align="right">16.65</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.79</td>
    <td align="right">18.61</td>
    <td align="right">17.43</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.29</td>
    <td align="right">9.43</td>
    <td align="right">9.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.08</td>
    <td align="right">26.80</td>
    <td align="right">23.76</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">22.23</td>
    <td align="right">27.42</td>
    <td align="right">27.78</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.98</td>
    <td align="right">18.24</td>
    <td align="right">18.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">48.97</td>
    <td align="right">42.10</td>
    <td align="right">52.55</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">60.76</td>
    <td align="right">63.94</td>
    <td align="right">62.34</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.11</td>
    <td align="right">24.69</td>
    <td align="right">26.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">40.14</td>
    <td align="right">48.63</td>
    <td align="right">50.98</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">79.48</td>
    <td align="right">73.99</td>
    <td align="right">48.76</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">41.80</td>
    <td align="right">46.05</td>
    <td align="right">51.11</td>
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
    <td align="right">6.97</td>
    <td align="right">9.61</td>
    <td align="right">9.96</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.75</td>
    <td align="right">16.99</td>
    <td align="right">18.99</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.38</td>
    <td align="right">18.13</td>
    <td align="right">17.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">12.09</td>
    <td align="right">23.64</td>
    <td align="right">19.85</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.51</td>
    <td align="right">23.43</td>
    <td align="right">24.59</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">19.05</td>
    <td align="right">22.92</td>
    <td align="right">22.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">25.09</td>
    <td align="right">22.63</td>
    <td align="right">26.37</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">42.00</td>
    <td align="right">48.95</td>
    <td align="right">47.24</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">40.83</td>
    <td align="right">35.92</td>
    <td align="right">35.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">44.22</td>
    <td align="right">48.63</td>
    <td align="right">48.00</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">57.88</td>
    <td align="right">68.93</td>
    <td align="right">83.91</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">85.62</td>
    <td align="right">75.77</td>
    <td align="right">75.61</td>
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
    <td align="right">42.26</td>
    <td align="right">8.57</td>
    <td align="right">6.60</td>
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
    <td align="right">59.25</td>
    <td align="right">57.68</td>
    <td align="right">44.06</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.81</td>
    <td align="right">23.11</td>
    <td align="right">27.25</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.11</td>
    <td align="right">25.88</td>
    <td align="right">29.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.19</td>
    <td align="right">83.12</td>
    <td align="right">46.18</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.69</td>
    <td align="right">23.94</td>
    <td align="right">26.63</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.17</td>
    <td align="right">28.26</td>
    <td align="right">30.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">109.77</td>
    <td align="right">100.21</td>
    <td align="right">43.58</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.12</td>
    <td align="right">24.90</td>
    <td align="right">26.64</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.65</td>
    <td align="right">31.87</td>
    <td align="right">31.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">139.66</td>
    <td align="right">123.32</td>
    <td align="right">43.95</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.49</td>
    <td align="right">27.36</td>
    <td align="right">27.94</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.94</td>
    <td align="right">32.37</td>
    <td align="right">33.78</td>
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
    <td align="right">23.66</td>
    <td align="right">42.73</td>
    <td align="right">42.79</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.12</td>
    <td align="right">43.19</td>
    <td align="right">43.55</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.63</td>
    <td align="right">24.85</td>
    <td align="right">24.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.19</td>
    <td align="right">58.41</td>
    <td align="right">58.71</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.20</td>
    <td align="right">59.81</td>
    <td align="right">59.14</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.53</td>
    <td align="right">36.31</td>
    <td align="right">25.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.33</td>
    <td align="right">80.65</td>
    <td align="right">80.14</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.95</td>
    <td align="right">81.29</td>
    <td align="right">83.48</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">28.92</td>
    <td align="right">54.91</td>
    <td align="right">39.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">43.64</td>
    <td align="right">88.76</td>
    <td align="right">89.12</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.18</td>
    <td align="right">96.78</td>
    <td align="right">94.86</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.32</td>
    <td align="right">55.60</td>
    <td align="right">40.06</td>
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
    <td align="right">18.66</td>
    <td align="right">26.15</td>
    <td align="right">26.09</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.68</td>
    <td align="right">28.99</td>
    <td align="right">28.96</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.86</td>
    <td align="right">30.77</td>
    <td align="right">30.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.92</td>
    <td align="right">46.80</td>
    <td align="right">34.82</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.43</td>
    <td align="right">39.87</td>
    <td align="right">27.53</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.09</td>
    <td align="right">51.81</td>
    <td align="right">40.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.63</td>
    <td align="right">54.29</td>
    <td align="right">38.86</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.00</td>
    <td align="right">53.00</td>
    <td align="right">35.16</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.14</td>
    <td align="right">61.05</td>
    <td align="right">44.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.76</td>
    <td align="right">55.19</td>
    <td align="right">39.83</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.67</td>
    <td align="right">64.52</td>
    <td align="right">44.66</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.21</td>
    <td align="right">64.98</td>
    <td align="right">44.33</td>
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
    <td align="right">61.95</td>
    <td align="right">35.83</td>
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
    <td align="right">66.86</td>
    <td align="right">61.69</td>
    <td align="right">48.00</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.26</td>
    <td align="right">23.27</td>
    <td align="right">28.91</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">27.80</td>
    <td align="right">29.56</td>
    <td align="right">32.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">97.00</td>
    <td align="right">87.28</td>
    <td align="right">49.23</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">26.79</td>
    <td align="right">24.79</td>
    <td align="right">27.72</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">30.36</td>
    <td align="right">30.36</td>
    <td align="right">33.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">123.28</td>
    <td align="right">108.44</td>
    <td align="right">46.55</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">28.42</td>
    <td align="right">26.96</td>
    <td align="right">28.29</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">34.26</td>
    <td align="right">35.83</td>
    <td align="right">36.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">187.45</td>
    <td align="right">160.63</td>
    <td align="right">51.45</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">35.11</td>
    <td align="right">31.86</td>
    <td align="right">32.85</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">39.28</td>
    <td align="right">42.40</td>
    <td align="right">41.82</td>
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
    <td align="right">25.52</td>
    <td align="right">43.41</td>
    <td align="right">43.39</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">29.68</td>
    <td align="right">43.99</td>
    <td align="right">44.38</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">19.85</td>
    <td align="right">29.05</td>
    <td align="right">29.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.45</td>
    <td align="right">59.24</td>
    <td align="right">59.43</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">36.79</td>
    <td align="right">61.31</td>
    <td align="right">60.90</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">18.81</td>
    <td align="right">40.11</td>
    <td align="right">29.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">43.73</td>
    <td align="right">82.51</td>
    <td align="right">82.49</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">50.20</td>
    <td align="right">84.41</td>
    <td align="right">84.54</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">33.52</td>
    <td align="right">64.16</td>
    <td align="right">46.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">55.77</td>
    <td align="right">99.99</td>
    <td align="right">98.44</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">70.47</td>
    <td align="right">109.18</td>
    <td align="right">127.68</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">57.11</td>
    <td align="right">90.23</td>
    <td align="right">68.81</td>
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
    <td align="right">19.95</td>
    <td align="right">31.60</td>
    <td align="right">30.99</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">21.87</td>
    <td align="right">33.23</td>
    <td align="right">33.13</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">21.98</td>
    <td align="right">35.31</td>
    <td align="right">36.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.25</td>
    <td align="right">53.44</td>
    <td align="right">40.72</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.22</td>
    <td align="right">41.57</td>
    <td align="right">30.33</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">22.16</td>
    <td align="right">58.47</td>
    <td align="right">48.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">38.59</td>
    <td align="right">69.63</td>
    <td align="right">49.74</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">45.13</td>
    <td align="right">61.56</td>
    <td align="right">40.81</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">36.51</td>
    <td align="right">68.21</td>
    <td align="right">52.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">48.10</td>
    <td align="right">85.87</td>
    <td align="right">53.95</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">42.48</td>
    <td align="right">78.89</td>
    <td align="right">59.98</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">42.12</td>
    <td align="right">81.44</td>
    <td align="right">63.18</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
